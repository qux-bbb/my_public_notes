# Message相关

```
GetMessage
查看消息，将消息从队列中移除，直到有消息才会有返回值，阻塞型函数

PeekMessage
查看消息，不会将消息从队列中移除，非阻塞型函数

TranslateMessage
转换消息，将虚拟键消息转换为字符消息，放到队列中，供GetMessage或PeekMessage读取

DispatchMessage
分发一个消息给窗口程序
```


2019/4/24  
