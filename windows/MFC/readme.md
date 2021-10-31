# MFC

MFC, Microsoft Foundation Class  

Microsoft基础类库（MFC）是用于在Microsoft Windows中编程的"应用程序框架"。MFC提供了很多代码，这些代码是以下代码所必需的：  
- 管理窗口
- 菜单和对话框
- 执行基本输入/输出
- 存储数据对象的集合等

通过将应用程序特定的代码添加到MFC框架中，可以很容易地扩展或覆盖C++应用程序中的MFC框架的基本功能。  

可以参考这个写简单的图形界面程序，感觉不好用。  
https://www.tutorialspoint.com/mfc/index.htm  


## 点击按钮弹窗

VS2019，创建"MFC 应用"项目，应用程序类型选择"基于对话框"，点击右下角"完成"即可。  
左边"工具箱"选择"Button"拖动到界面，双击Button1，可以跳到代码执行逻辑，如下：  
```cpp
void CMFCApplication1Dlg::OnBnClickedButton1()
{
	// TODO: 在此添加控件通知处理程序代码
}
```
在函数中添加 `CWnd::MessageBox(L"Hello World");`，保存，生成解决方案即可。  

注意：千万不要在Button1右键选择"添加事件处理程序"，莫名其妙的错误。  


## 其它
用户名需要的组件有`Static Text`, `Edit Control`  
如果需要获取`Edit Control`组件中输入的内容，需要在组件上右键选择"添加变量"，比如命名为`theCEdit1`，然后在某个Button的点击处理函数中添加这样的代码：  
```cpp
CString string1;
theCEdit1.GetWindowTextW(string1);
```
这样string1就存储了`Edit Control`组件中输入的内容  


---
2021/6/13  
