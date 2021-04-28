## VS2017使用OLLVM

生成一个OLLVM项目：  
```bat
git clone -b llvm-4.0 https://github.com/obfuscator-llvm/obfuscator
cd obfuscator
mkdir build
cd build
cmake -G "Visual Studio 15 2017 Win64" ..
```
注意cmake命令需要在 `VS 2017的开发人员命令提示符` 下运行  

找到 `D:\obfuscator\include\llvm\Support\ManagedStatic.h`，添加一个宏定义：  
`#define ENDIAN_LITTLE`  

使用VS2017把build文件夹打开，开始编译(时间比较久)  
默认编译完成后，可执行文件目录: `D:\obfuscator\build\Debug\bin`  

VS2017 工具->扩展和更新->联机，搜索"llvm"，安装`LLVM Compiler Toolchain`  

新建一个项目，用这个当源码测试：  
```cpp
#include <Windows.h>

int main()
{
	int a = GetTickCount64();
	int b = a % 10;
	int c = 0;
	for (int i = 0; i < b; i++)
	{
		c += a % i;
	}
	return c;
}
```
项目->项目属性->配置属性->常规->平台工具集，选择"llvm"，点击"应用"，这样可以出现LLVM配置项  

配置属性->LLVM，把clang-cl路径替换成ollvm相应路径，如：  
`D:\obfuscator\build\Debug\bin\clang-cl.exe`  
`Use lld-link` 和 `Use llvm-lib` 先设为"否"  

配置属性->C/C++->命令行->其他选项，设置混淆参数  
指令替换(Instructions substitution)示例：  
```
-mllvm -sub -mllvm -sub_loop=5 -mllvm -aesSeed=1234567890ABCDEF1234567890ABCDEF
```
虚假控制流程(Bogus control flow)示例：  
```
-mllvm -bcf -mllvm -aesSeed=1234567890ABCDEF1234567890ABCDEF 
```
控制流平坦化(Control flow flattening)示例：  
```
-mllvm -fla -mllvm -aesSeed=1234567890ABCDEF1234567890ABCDEF
```
综合一下：  
```
-mllvm -sub -mllvm -bcf -mllvm -fla -mllvm -aesSeed=1234567890ABCDEF1234567890ABCDEF
```

重新生成解决方案，即可得到被混淆的可执行文件  
可以把混淆参数去掉 重新生成解决方案，对比一下，混淆效果明显  
混淆参数可以自己设置  

- - - -
生成解决方案可能出现的错误：  
```
no such file or directory: '/JMC'
no such file or directory: '/diagnostics:classic'
no such file or directory: '/permissive-'
```
去掉这些选项就好了：  
```
项目->项目属性->配置属性->C/C++->常规->支持仅我的代码调试，设置为"否"
项目->项目属性->配置属性->C/C++->常规->诊断格式，删除
项目->项目属性->配置属性->C/C++->语言->符合模式，设置为"否"
```
- - - -
相关链接：  
https://0xpat.github.io/Malware_development_part_6/  
https://github.com/obfuscator-llvm/obfuscator/wiki/  
https://llvm.org/builds/  


2021/4/28  
