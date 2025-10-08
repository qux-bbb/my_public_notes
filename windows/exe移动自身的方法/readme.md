# exe移动自身的方法

## MoveFile
```cpp
#include <windows.h>
#include <iostream>
#include <string>

int main() {
    // 获取当前可执行文件的路径
    char currentPath[MAX_PATH];
    GetModuleFileNameA(NULL, currentPath, MAX_PATH);

    // 目标文件夹路径
    std::string targetDir = "MyAppFolder\\";

    // 创建目标文件夹（如果不存在）
    CreateDirectoryA(targetDir.c_str(), NULL);

    // 构建目标文件路径
    std::string targetPath = targetDir + "myapp.exe";

    // 尝试移动文件
    if (MoveFileA(currentPath, targetPath.c_str())) {
        std::cout << "文件移动成功！" << std::endl;
        std::cout << "从: " << currentPath << std::endl;
        std::cout << "到: " << targetPath << std::endl;
    }
    else {
        DWORD error = GetLastError();
        std::cout << "文件移动失败！错误代码: " << error << std::endl;

        // 常见的错误处理
        switch (error) {
        case ERROR_FILE_NOT_FOUND:
            std::cout << "源文件未找到" << std::endl;
            break;
        case ERROR_ACCESS_DENIED:
            std::cout << "访问被拒绝（可能文件正在运行）" << std::endl;
            break;
        case ERROR_ALREADY_EXISTS:
            std::cout << "目标文件已存在" << std::endl;
            break;
        default:
            std::cout << "未知错误" << std::endl;
        }
    }

    return 0;
}
```

## cmd的move命令
```cpp
#include <windows.h>
#include <string>
#include <iostream>

int main() {
    // 获取当前可执行文件的路径
    char currentPath[MAX_PATH];
    GetModuleFileNameA(NULL, currentPath, MAX_PATH);

    // 目标文件夹路径
    std::string targetDir = "MyAppFolder";
    std::string targetPath = targetDir + "\\" + std::string(currentPath).substr(std::string(currentPath).find_last_of("\\") + 1);

    // 创建目标文件夹
    CreateDirectoryA(targetDir.c_str(), NULL);

    // 构建move命令
    std::string moveCommand = "cmd /c move \"" + std::string(currentPath) + "\" \"" + targetPath + "\"";

    std::cout << "执行命令: " << moveCommand << std::endl;

    // 执行move命令
    int result = system(moveCommand.c_str());

    if (result == 0) {
        std::cout << "文件移动成功!" << std::endl;
    }
    else {
        std::cout << "文件移动失败! 错误码: " << result << std::endl;
    }

    return 0;
}
```


---
2025/10/8
