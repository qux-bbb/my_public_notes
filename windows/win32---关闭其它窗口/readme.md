# win32---关闭其它窗口

在WndProc函数中，添加2个case  

```c
case WM_CREATE:
		SetTimer(hWnd, 1, 1000, NULL);           //设置定时器,每秒调用一次。
		break;

case WM_TIMER:
	{
		// HH Parent  一个文档类
		// TXGuiFoundation  QQ类
		HWND hwTsk = FindWindow(_T("HH Parent"),NULL); 
		if (hwTsk != NULL)
		{
			PostMessage(hwTsk, WM_CLOSE, NULL, NULL);          
		}
		break;
	}

```

每隔1s，就会检测是否存在此类，存在则关闭  

找类方法：  
打开窗口，用VS的工具中的spy++  
搜索→查找窗口，拖到窗口上就可以找到类了  

win10下测试能关闭普通窗口，可以关闭QQ，但是关不掉任务管理器  

win7可以关闭任务管理器  


2017/9/8  
