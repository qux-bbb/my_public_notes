# SystemParametersInfoA设置壁纸

SystemParametersInfoA可以设置壁纸，原理是设置注册表项：  
```r
HKEY_CURRENT_USER\Control Panel\Desktop\Wallpaper

# 手动查看时，注册表里先进入目录 HKEY_CURRENT_USER\Control Panel\Desktop 再查看 Wallpaper 项
```

代码：  
```cpp
#include <Windows.h>
#include <iostream>

int main() {
    // Specify the full path of the wallpaper file
    // 这里注意必须是绝对路径，win7支持jpg、bmp，不支持png
    const char* wallpaperPath = "C:\\path\\to\\your\\wallpaper.jpg";

    // Call the SystemParametersInfo function to set the wallpaper
    // SPIF_UPDATEINIFILE 标志会使更改永久保存，而 SPIF_SENDCHANGE 标志则会发送系统消息通知所有顶级窗口
    if (SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, (PVOID)wallpaperPath, SPIF_UPDATEINIFILE | SPIF_SENDCHANGE)) {
        std::cout << "Wallpaper set successfully!\n";
    }
    else {
        DWORD dwError = GetLastError();
        std::cout << "Failed to set wallpaper! Error code: " << dwError << "\n";
    }

    // Wait for the user to enter a random value
    int value;
    std::cout << "Enter any integer to exit: ";
    std::cin >> value;

    return 0;
}
```

来源: chatgpt  


2023/10/22  
