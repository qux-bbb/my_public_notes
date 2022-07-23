# 写vscode扩展的流程

## 写扩展
这是官方教程：https://code.visualstudio.com/api  
这是官方的例子：https://github.com/microsoft/vscode-extension-samples  

开发：  
1. 安装nodejs  
2. 安装必要的包：`npm install -g yo generator-code`  
3. 生成基本的结构：`yo code`  
4. vscode写扩展代码  
5. 调试查看功能是否正常  


## 发布扩展
官方的发布包流程已经不适用了，不要做任何和dev.azure.com有关的操作  
需要点下面链接登录(用微软账户)，创建publishers（是人的名字，不是项目的名字）  
https://marketplace.visualstudio.com/manage/publishers  

把自己的项目传到github  

在package.json中加2个顶级字段，大概是这样：  
```r
{
    
    ...
	"publisher": "my_name",
    ...
	"repository": {
        "type": "git",
        "url": "https://github.com/my_name/hello"
    },
    ...
}
```
建议publisher和github的名字对应，虽然不是必要的。  


安装vsce（"Visual Studio Code Extensions"，一个打包发布管理扩展的工具），打包：  
```sh
cd myExtension
npm install vsce
vsce package
```
会生成一个vsix结尾的文件  

在自己的publisher地址上传自己的扩展，等待发布  
https://marketplace.visualstudio.com/manage/publishers/my_name  

发布完，就能在扩展窗口搜到自己的扩展了。  


## 相关资料
增加扩展配置功能：  
1. https://code.visualstudio.com/api/references/when-clause-contexts#conditional-operators
2. https://code.visualstudio.com/api/references/extension-guidelines#settings
3. https://code.visualstudio.com/api/references/contribution-points#contributes.configuration
4. https://github.com/yzhang-gh/vscode-markdown/blob/master/package.nls.zh-cn.json
5. https://github.com/eamodio/vscode-gitlens/blob/main/package.json


20201129  
