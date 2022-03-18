# rust---使用vscode调试代码

rust现在没有独立的IDE，调试功能也不是太好用，vscode勉强支持调试，需要结合cargo使用。  
vscode安装Rust扩展。  

使用cargo**创建并构建**一个项目，然后用vscode打开新生成的文件夹  

Debug -> Add Configuration  
Windows上选择 `C++ (Windows)`  
Mac或Linux上选择 `LLDB: Custom Launch`  

修改launch.json中对应的program参数为debug程序的路径，如: `${workspaceRoot}/target/debug/foo.exe`  

在设置中搜索"break", 勾选"Allow setting breakpoints in any file"  

这样就可以在源码下断点进行调试了  
如果修改了源码，需要手动执行 `cargo build` 生成新的debug程序，再去调试  


参考链接: https://www.forrestthewoods.com/blog/how-to-debug-rust-with-visual-studio-code  

rust-analyzer 比 Rust 扩展更好用，参数类型提示效果较好，调试不需要手动修改json配置文件。  


2022/2/19  
