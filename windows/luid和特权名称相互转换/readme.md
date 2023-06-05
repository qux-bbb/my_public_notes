# luid和特权名称相互转换

特权名称举例如:  
SeBackupPrivilege  

luid和特权名称不是固定对应的关系, 需要通过api去查询转换  

通过特权名称查询luid  
```c++
BOOL LookupPrivilegeValueW(
  LPCWSTR lpSystemName,
  LPCWSTR lpName,
  PLUID   lpLuid
);
```

通过luid查询特权名称  
```c++
BOOL LookupPrivilegeNameW(
  LPCWSTR lpSystemName,
  PLUID   lpLuid,
  LPWSTR  lpName,
  LPDWORD cchName
);
```

参考链接:  
1. cnblogs.com/debug-me/p/6931477.html  
2. https://docs.microsoft.com/zh-cn/windows/win32/api/winbase/nf-winbase-lookupprivilegevaluew  
3. https://docs.microsoft.com/zh-cn/windows/win32/api/winbase/nf-winbase-lookupprivilegenamew  


2019/12/13  
