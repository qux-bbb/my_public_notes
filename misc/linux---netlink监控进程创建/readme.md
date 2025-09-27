# linux---netlink监控进程创建

使用 Linux 的 Netlink 套接字（`AF_NETLINK`）实现内核与用户空间的通信，具体通过 `NETLINK_CONNECTOR` 协议来监控进程事件。  
利用 Linux 的 Connector 子系统和 PROC 事件机制（`CN_IDX_PROC`/`CN_VAL_PROC`）来订阅和捕获进程执行事件（`PROC_EVENT_EXEC`）。

[process_monitor.cpp](./files/process_monitor.cpp)


2025/9/27
