# oletools

github地址: https://github.com/decalage2/oletools  

oletools是一个python工具包，用于分析Microsoft OLE2文件，如Microsoft Office文档或Outlook消息，主要用于恶意软件分析、取证和调试。  

安装: `pip install -U oletools`  

其中的 olevba 用来从文件中提取和分析VBA宏代码，示例：  
```r
# 扫描单个文件
olevba file.doc
# 扫描单个文件 显示解码之后的混淆字符串
olevba file.doc --decode
# 扫描单个文件 显示经过字符串反混淆之后的VBA宏代码
olevba file.doc --reveal
```


2021/12/27  
