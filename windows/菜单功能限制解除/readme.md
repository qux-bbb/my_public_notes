# 菜单功能限制解除

相关api为  
```
EnableMenuItem
EnableWindow
```

定义  
```c
BOOL EnableMenuItem(
  HMENU hMenu,
  UINT  uIDEnableItem,
  UINT  uEnable
);
```

uEnable取值含义  
```
Value Meaning
MF_BYCOMMAND/0x00000000L Indicates that uIDEnableItem gives the identifier of the menu item. If neither the MF_BYCOMMAND nor MF_BYPOSITION flag is specified, the MF_BYCOMMAND flag is the default flag.
MF_BYPOSITION/0x00000400L Indicates that uIDEnableItem gives the zero-based relative position of the menu item.
MF_DISABLED/0x00000002L Indicates that the menu item is disabled, but not grayed, so it cannot be selected.
MF_ENABLED/0x00000000L Indicates that the menu item is enabled and restored from a grayed state so that it can be selected.
MF_GRAYED/0x00000001L Indicates that the menu item is disabled and grayed so that it cannot be selected.
```

MSDN相关链接: https://docs.microsoft.com/zh-cn/windows/win32/api/winuser/nf-winuser-enablemenuitem?redirectedfrom=MSDN  


2019/11/24  
