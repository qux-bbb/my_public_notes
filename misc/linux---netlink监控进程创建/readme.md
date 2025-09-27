# linux---netlink监控进程创建

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
g++ -o process_monitor process_monitor.cpp
```

运行：
```bash
sudo ./process_monitor
```


2025/9/27
