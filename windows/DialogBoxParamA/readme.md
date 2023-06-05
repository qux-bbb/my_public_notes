# DialogBoxParamA

```c++
INT_PTR DialogBoxParamA(
  HINSTANCE hInstance,
  LPCSTR    lpTemplateName,
  HWND      hWndParent,
  DLGPROC   lpDialogFunc,
  LPARAM    dwInitParam
);
```

lpTemplateName 和 lpDialogFunc比较重要  

lpTemplateName 指向资源模板  
lpDialogFunc 处理函数  

可以用eXeScope, Resource Hacker查看资源  


2019/11/19  
