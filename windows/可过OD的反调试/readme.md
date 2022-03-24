# 可过OD的反调试

```c
// CheckRemoteDebuggerPresent 反调试，OD插件不能直接忽略
BOOL HasDebugPort = FALSE;
CheckRemoteDebuggerPresent(GetCurrentProcess(), &HasDebugPort);
if (HasDebugPort)
	exit(0);
```


2019/8/28  
