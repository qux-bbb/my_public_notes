# python---跨平台检测是否有管理员权限

```python
import ctypes, os
try:
    is_admin = os.getuid() == 0
except AttributeError:
    is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

print is_admin
```

原链接：https://stackoverflow.com/questions/1026431/cross-platform-way-to-check-admin-rights-in-a-python-script-under-windows  


2020/12/8  
