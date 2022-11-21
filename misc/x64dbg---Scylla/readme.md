# x64dbg---Scylla

https://github.com/x64dbg/Scylla  
Scylla是x64dbg内置的插件，不需要自己安装，可用于dump进程，导入表修复。  

正常流程：  
1. 调试器运行相应程序到oep
2. 插件 -> Scylla, 打开这个插件
3. 右下角 Dump -> Dump, 使用Scylla dump进程
4. 左下角 IAT Info 中，依次点击 IAT Autosearch, Get Imports 找到并获取导入表
5. 右下角 Dump -> Fix Dump, 选择第3步dump出的文件，即可修复导入表

第4步的 IAT Autosearch 有2种模式: advanced search, normal search, 看哪种找到的导入表项多就选哪个吧，可以都试一下，重试之前记得在Imports框的右下角点一下 Clear  

如果 IAT Autosearch 遇到问题，做如下操作：  
1. 如果视野中有明显的api调用，就找到对应行，右键 内存转到call的目标函数地址，选择显示模式为'地址'；如果没有，可以右键查看模块间的函数调用，然后随便找一个系统函数，回车到代码区域，继续做之前的操作
2. 向上翻可以找到api地址名称映射的开头（VA），界定是否为开头，就是看看前面有没有api地址名称映射了 
3. 接着翻到最下面计算Size（下面减去上面），比如第1条的地址是0x414000, 最后一条的地址是0x4143B4, 那Size就是0x4143B4-0x414000+4=0x3B8
4. 在Scylla的 IAT Info 中手动填写 VA 和 Size, 然后就可以继续正常流程的第4步中的 Get Imports 了

如果 Get Imports 遇到问题，可能会遇到一些无效的导入表项，解决方法如下：  
Imports 的左下角，点击 Show Invalid, 然后在 Imports 中选中无效的项，右键 Cut thunk 即可  
