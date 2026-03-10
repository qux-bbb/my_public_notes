# linux---netlink监控进程创建

keywords: procmon

## process_monitor
功能说明：
- 使用Linux Netlink接口监控进程执行事件（exec）
- 获取新创建进程的详细信息
  - 进程ID (PID)
  - 进程名
  - 进程可执行文件路径
  - 完整命令行

代码: [process_monitor.cpp](./files/process_monitor.cpp)

编译：
```bash
g++ -std=c++11 -o process_monitor process_monitor.cpp
```

运行：
```bash
sudo ./process_monitor
# 输出到屏幕和日志文件
sudo ./process_monitor 2>&1 | tee process_monitor.log
```

## current_and_new_process_monitor
先输出当前所有进程，再监控新进程: [current_and_new_process_monitor.cpp](./files/current_and_new_process_monitor.cpp)

编译：
```bash
g++ -std=c++11 -o current_and_new_process_monitor current_and_new_process_monitor.cpp
```

运行：
```bash
sudo ./current_and_new_process_monitor
# 输出到屏幕和日志文件
sudo ./current_and_new_process_monitor 2>&1 | tee current_and_new_process_monitor.log
```
