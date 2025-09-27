#include <iostream>
#include <string>
#include <cstring>
#include <sys/socket.h>
#include <linux/netlink.h>
#include <linux/connector.h>
#include <linux/cn_proc.h>
#include <unistd.h>
#include <fstream>
#include <signal.h>
#include <ctime>
#include <limits.h>

struct ProcessInfo {
    pid_t pid;
    std::string process_name;
    std::string process_path;  // 进程可执行文件的完整路径
    std::string cmdline;
};

class ProcessMonitor {
public:
    ProcessMonitor() : netlink_fd(-1) {}
    ~ProcessMonitor() {
        if (netlink_fd >= 0) {
            close(netlink_fd);
        }
    }

    int netlink_fd;
    static bool running;

    bool start() {
        if (!init_netlink()) {
            return false;
        }

        // 设置信号处理
        signal(SIGINT, signal_handler);
        signal(SIGTERM, signal_handler);
        running = true;

        std::cout << "进程监控工具已启动，正在监控进程创建事件..." << std::endl;
        std::cout << "按Ctrl+C停止监控" << std::endl;

        char buffer[4096];
        while (running) {
            ssize_t len = recv(netlink_fd, buffer, sizeof(buffer), 0);
            if (len < 0) {
                if (!running)
                    break; // 正常退出
                perror("recv");
                break;
            }

            struct nlmsghdr *nh = (struct nlmsghdr *)buffer;
            for (; NLMSG_OK(nh, len); nh = NLMSG_NEXT(nh, len)) {
                if (nh->nlmsg_type == NLMSG_DONE) {
                    struct cn_msg *cn = (struct cn_msg *)NLMSG_DATA(nh);
                    if (cn->id.idx == CN_IDX_PROC && cn->id.val == CN_VAL_PROC) {
                        struct proc_event *event = (struct proc_event *)cn->data;

                        if (event->what == PROC_EVENT_EXEC) {
                            pid_t target_pid = event->event_data.exec.process_pid;
                            // 获取并显示进程信息
                            ProcessInfo proc_info = get_process_info(target_pid);
                            if (!proc_info.process_name.empty()) {
                                // 显示进程信息
                                std::cout << "\n=== 检测到新进程 ===" << std::endl;
                                std::cout << "进程ID: " << proc_info.pid << std::endl;
                                std::cout << "进程名: " << proc_info.process_name << std::endl;
                                std::cout << "进程路径: " << (proc_info.process_path.empty() ? "未知" : proc_info.process_path) << std::endl;
                                std::cout << "完整命令行: " << proc_info.cmdline << std::endl;
                            }
                        }
                    }
                }
            }
        }

        return true;
    }

    static void signal_handler(int sig) {
        if (sig == SIGINT || sig == SIGTERM) {
            running = false;
            std::cout << "\n正在停止进程监控工具..." << std::endl;
        }
    }

    bool init_netlink() {
        netlink_fd = socket(AF_NETLINK, SOCK_DGRAM, NETLINK_CONNECTOR);
        if (netlink_fd < 0) {
            perror("socket");
            return false;
        }

        // 检查并设置系统参数
        std::ifstream rmem_file("/proc/sys/net/core/rmem_max");
        if (rmem_file.is_open()) {
            std::string rmem_max_str;
            std::getline(rmem_file, rmem_max_str);
            rmem_file.close();

            int rmem_max = 0;
            try {
                rmem_max = std::stoi(rmem_max_str);
            } catch (const std::exception &e) {
                std::cerr << "致命错误: 无法解析系统rmem_max值: '" << rmem_max_str << "'" << std::endl;
                std::cerr << "程序终止" << std::endl;
                exit(1);
            }

            if (rmem_max < 4194304) { // 4MB
                std::string cmd = "echo 4194304 > /proc/sys/net/core/rmem_max";
                int result = system(cmd.c_str());
            }
        }

        // 设置socket接收缓冲区大小
        int rcv_buf_size = 4 * 1024 * 1024; // 4MB
        if (setsockopt(netlink_fd, SOL_SOCKET, SO_RCVBUF, &rcv_buf_size, sizeof(rcv_buf_size)) < 0) {
            perror("setsockopt SO_RCVBUF");
        } else {
            // 验证实际设置的大小
            int actual_size;
            socklen_t len = sizeof(actual_size);
            if (getsockopt(netlink_fd, SOL_SOCKET, SO_RCVBUF, &actual_size, &len) == 0) {
                std::cout << "接收缓冲区设置成功: 请求=" << std::to_string(rcv_buf_size / 1024) <<
                          "KB, 实际=" << std::to_string(actual_size / 1024) << "KB" << std::endl;
            }
        }

        // 设置socket发送缓冲区大小
        int snd_buf_size = 1024 * 1024; // 1MB
        if (setsockopt(netlink_fd, SOL_SOCKET, SO_SNDBUF, &snd_buf_size, sizeof(snd_buf_size)) < 0) {
            perror("setsockopt SO_SNDBUF");
        } else {
            int actual_size;
            socklen_t len = sizeof(actual_size);
            if (getsockopt(netlink_fd, SOL_SOCKET, SO_SNDBUF, &actual_size, &len) == 0) {
                std::cout << "发送缓冲区设置成功: 请求=" << std::to_string(snd_buf_size / 1024) <<
                          "KB, 实际=" << std::to_string(actual_size / 1024) << "KB" << std::endl;
            }
        }

        struct sockaddr_nl addr;
        memset(&addr, 0, sizeof(addr));
        addr.nl_family = AF_NETLINK;
        addr.nl_pid = getpid();
        addr.nl_groups = CN_IDX_PROC;

        if (bind(netlink_fd, (struct sockaddr *)&addr, sizeof(addr)) < 0) {
            perror("bind");
            close(netlink_fd);
            return false;
        }

        // 订阅进程事件
        struct nlmsghdr nh;
        struct cn_msg cn;
        enum proc_cn_mcast_op op;

        memset(&nh, 0, sizeof(nh));
        memset(&cn, 0, sizeof(cn));

        nh.nlmsg_len = NLMSG_LENGTH(sizeof(cn) + sizeof(op));
        nh.nlmsg_type = NLMSG_DONE;
        nh.nlmsg_flags = 0;
        nh.nlmsg_seq = 0;
        nh.nlmsg_pid = getpid();

        cn.id.idx = CN_IDX_PROC;
        cn.id.val = CN_VAL_PROC;
        cn.len = sizeof(op);

        op = PROC_CN_MCAST_LISTEN;

        // 构造完整的消息
        char msg_buf[NLMSG_LENGTH(sizeof(cn) + sizeof(op))];
        memcpy(msg_buf, &nh, sizeof(nh));
        memcpy(NLMSG_DATA((struct nlmsghdr *)msg_buf), &cn, sizeof(cn));
        memcpy((char *)NLMSG_DATA((struct nlmsghdr *)msg_buf) + sizeof(cn), &op, sizeof(op));

        if (send(netlink_fd, msg_buf, nh.nlmsg_len, 0) < 0) {
            perror("send");
            close(netlink_fd);
            return false;
        }

        return true;
    }

    std::string read_link(const std::string &path) {
        char buffer[PATH_MAX];
        ssize_t len = readlink(path.c_str(), buffer, sizeof(buffer) - 1);
        if (len == -1) {
            return "";
        }
        buffer[len] = '\0';
        return std::string(buffer);
    }

    ProcessInfo get_process_info(pid_t pid) {
        ProcessInfo info;
        info.pid = pid;

        // 获取进程名和路径，使用 /proc/PID/exe 获取真正的可执行文件路径
        std::string exe_path = "/proc/" + std::to_string(pid) + "/exe";
        std::string exe_link = read_link(exe_path);
        if (!exe_link.empty()) {
            // 存储完整路径
            info.process_path = exe_link;
            // 提取文件名部分
            size_t slash_pos = exe_link.find_last_of('/');
            if (slash_pos != std::string::npos) {
                info.process_name = exe_link.substr(slash_pos + 1);
            } else {
                info.process_name = exe_link;
            }
        }

        // 读取命令行
        std::string cmdline_raw;
        std::ifstream cmdline_file("/proc/" + std::to_string(pid) + "/cmdline");
        if (cmdline_file.is_open()) {
            std::getline(cmdline_file, cmdline_raw);
            // 替换null字符为空格用于显示
            info.cmdline = cmdline_raw;
            for (char &c : info.cmdline) {
                if (c == '\0')
                    c = ' ';
            }
        }

        return info;
    }
};

// 定义静态成员变量
bool ProcessMonitor::running = false;

int main() {
    ProcessMonitor monitor;
    
    if (!monitor.start()) {
        std::cerr << "进程监控工具启动失败" << std::endl;
        return 1;
    }
    
    return 0;
}