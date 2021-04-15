读写注册表项  

```c++
#include <Windows.h>
#include <stdio.h>


int main() {
    HKEY hKey;
    RegCreateKey(HKEY_CLASSES_ROOT, L"exefile\\shell\\open\\hello", &hKey);
    RegOpenKey(HKEY_CLASSES_ROOT, L"exefile\\shell\\open\\hello", &hKey);
    // 宽字符，而且要包括结尾0，所以: 11*2+1*2=24
    RegSetValue(hKey, NULL, REG_SZ, L"hello_value", 24);  // 不设置子键
    RegSetKeyValue(hKey, NULL, L"world", REG_SZ, L"world_value_haha", 34);  // 设置子键
    RegCloseKey(hKey);

    TCHAR firstBuffer[50] = { 0 };
    DWORD firstSize = sizeof(firstBuffer);
    RegGetValue(HKEY_CLASSES_ROOT, L"exefile\\shell\\open\\hello", NULL, RRF_RT_REG_SZ, NULL, (PVOID)firstBuffer, &firstSize);
    wprintf(L"firstBuffer: %s, firstSize: %d\n", firstBuffer, firstSize);

    TCHAR secondBuffer[50] = { 0 };
    DWORD secondSize = sizeof(secondBuffer);
    RegGetValue(HKEY_CLASSES_ROOT, L"exefile\\shell\\open\\hello", L"world", RRF_RT_REG_SZ, NULL, (PVOID)secondBuffer, &secondSize);
    wprintf(L"secondBuffer: %s, secondSize: %d\n", secondBuffer, secondSize);

    return 0;
}
```

参考链接：  
1. RegOpenKeyA: https://docs.microsoft.com/en-us/windows/win32/api/winreg/nf-winreg-regopenkeya  
2. RegSetValueA: https://docs.microsoft.com/en-us/windows/win32/api/winreg/nf-winreg-regsetvaluea  
3. RegGetValueA: https://docs.microsoft.com/en-us/windows/win32/api/winreg/nf-winreg-reggetvaluea  
4. 检查键是否存在: https://stackoverflow.com/questions/19579357/check-if-the-key-already-exists-regopenkey  
5. 确认RegGetValueA是否失败: https://stackoverflow.com/questions/26069085/visual-c-reggetvalue-fails-in-program-where-it-shouldnt  
6. RegGetValue例子: https://github.com/surpriserom/Pilotage-automatique-d-un-voilier-via-un-bus-CAN-Arduino/blob/6ecc8f118443953e96d93de45ab408165201e2b7/Source/serial-communication-manager-master/com.embeddedunveiled.native/windows_serial/windows_serial/windows_serial_driver_name.c  


20201211  
