# 设置窗口不可见的2种方式

keywords: 隐藏窗口  

## 方法1  
只使用ShowWindow  
```c
ShowWindow(hWnd, WS_VISIBLE);
```

## 方法2
在ShowWindow后使用SetWindowPos  
```c
ShowWindow(hWnd, nCmdShow);

SetWindowPos(hWnd, 0, 0, 0, 0, 0, SWP_HIDEWINDOW);
```

参考链接:  
1. https://docs.microsoft.com/zh-cn/windows/win32/winmsg/window-styles  
2. https://docs.microsoft.com/zh-cn/windows/win32/api/winuser/nf-winuser-showwindow?redirectedfrom=MSDN  
3. https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-setwindowpos  


2019/11/25  
