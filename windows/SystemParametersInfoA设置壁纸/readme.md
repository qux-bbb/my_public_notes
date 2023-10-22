# SystemParametersInfoA设置壁纸

```cpp
#include <Windows.h>
#include <iostream>

int main() {
    // Specify the full path of the wallpaper file
    // 这里注意必须是绝对路径，win7支持jpg、bmp，不支持png
    const char* wallpaperPath = "C:\\path\\to\\your\\wallpaper.jpg";

    // Call the SystemParametersInfo function to set the wallpaper
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
