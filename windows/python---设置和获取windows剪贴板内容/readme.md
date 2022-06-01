# python---设置和获取windows剪贴板内容

```python
# coding:utf8

# 参考 https://programtalk.com/python-examples/ctypes.windll.user32.OpenClipboard/

import ctypes


def get_clipboard_contents():
    CF_TEXT = 1
    ctypes.windll.user32.OpenClipboard(None)
    pcontents = ctypes.windll.user32.GetClipboardData(CF_TEXT)
    data = ctypes.c_char_p(pcontents).value
    ctypes.windll.user32.CloseClipboard()
    return data


def set_clipboard_contents(text):
    GHND = 0x0042
    CF_TEXT = 1
    ctypes.windll.user32.OpenClipboard(None)
    ctypes.windll.user32.EmptyClipboard()
    hcd = ctypes.windll.kernel32.GlobalAlloc(GHND, len(text) + 1)
    pcontents = ctypes.windll.kernel32.GlobalLock(hcd)
    ctypes.cdll.msvcrt.strcpy(ctypes.c_char_p(pcontents), text)
    ctypes.windll.kernel32.GlobalUnlock(hcd)
    ctypes.windll.user32.SetClipboardData(CF_TEXT, hcd)
    ctypes.windll.user32.CloseClipboard()

set_clipboard_contents('ccccc')
result = get_clipboard_contents()
print(result)
```


2020/9/24  
