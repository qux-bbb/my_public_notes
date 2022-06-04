# python2---ctypes找窗口

```python
# coding:utf8

from ctypes import *

KERNEL32 = windll.kernel32
USER32 = windll.user32

# 如果用到其他值, 需要查询MSDN
WM_GETTEXT = 0x0000000D
WM_GETTEXTLENGTH = 0x0000000E


class POINT(Structure):
    _fields_ = [('x', c_int), ('y', c_int)]


EnumWindowsProc = WINFUNCTYPE(c_bool, POINTER(c_int), POINTER(c_int))
EnumChildProc = WINFUNCTYPE(c_bool, POINTER(c_int), POINTER(c_int))


def foreach_child(hwnd, lparam):
    classname = create_unicode_buffer(50)
    USER32.GetClassNameW(hwnd, classname, 50)

    length = USER32.SendMessageW(hwnd, WM_GETTEXTLENGTH, 0, 0)
    text = create_unicode_buffer(length + 1)
    USER32.SendMessageW(hwnd, WM_GETTEXT, length + 1, text)
    print('hwnd: %r, classname: %r, text: %r' % (hex(addressof(hwnd)) , classname.value, text.value))

    return True

def foreach_window(hwnd, lparam):
    if USER32.IsWindowVisible(hwnd):
        print('=' * 40)
        print('head')
        foreach_child(hwnd, lparam)
        print('-'*40)
        USER32.EnumChildWindows(hwnd, EnumChildProc(foreach_child), 0)
    return True


def foreach_window_by_pid(hwnd, lparam):
    lpdwProcessId = c_long()
    USER32.GetWindowThreadProcessId(hwnd, byref(lpdwProcessId))

    if lpdwProcessId.value == lparam.contents.value:
        print('=' * 40)
        print('head')
        foreach_child(hwnd, lparam)
        print('-'*40)
        USER32.EnumChildWindows(hwnd, EnumChildProc(foreach_child), 0)
    return True

def main(f=0):
    if f == 0:
        # 所有可见窗口
        USER32.EnumWindows(EnumWindowsProc(foreach_window), 0)
    elif f == 1:
        # 指定位置的可见窗口
        want_hwnd = USER32.WindowFromPoint(POINT(300, 200))
        if want_hwnd:
            foreach_window(want_hwnd, 0)
    elif f == 2:
        # 指定进程id的窗口
        pid = c_long(10836)
        lparam = pointer(pid)
        USER32.EnumWindows(EnumWindowsProc(foreach_window_by_pid), lparam)

if __name__ == '__main__':
    main(2)
```

参考:  
https://stackoverflow.com/questions/11711417/get-hwnd-by-process-id-c  


2019/12/17  
