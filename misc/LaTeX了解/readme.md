# LaTeX了解

LaTeX是一种高质量的排版系统；它包括为制作技术和科学文档而设计的功能。LaTeX是传播和出版科学文献的事实标准。  


## 下载安装
下载tex live 做后端（用iso镜像，在线安装太慢了）  
http://www.tug.org/texlive/acquire-iso.html >  
http://mirror.ctan.org/systems/texlive/Images/  

TeXstudio 或者vscode的LaTeX Workshop扩展 做前端  
https://www.texstudio.org/  

这里是一个简单的安装步骤：  
https://zhuanlan.zhihu.com/p/56982388?from_voters_page=true  
安装需要50分钟左右  


## 简介
这个简单的视频教程还不错  
https://www.bilibili.com/video/BV12t411A73w  
这里是一个简单的模板  
```tex
% 以'%'开头的行是注释
\documentclass[UTF8]{ctexart}
\title{世界你好}
\author{rvy}
\begin{document}
    \maketitle
    \tableofcontents
    \begin{abstract}
        这是摘要呀，这是摘要呀，这是摘要呀，这是摘要呀，这是摘要呀。
    \end{abstract}
    \section{引言}
    哈哈哈哈哈
    \section{内容}
    \LaTeX，这是LaTex的标志

    行内公式：$v=v_0+at$

    块状公式：
    \[
        x=v_0t+\frac{1}{2}at^2  
    \]
\end{document}
```


---
2020/9/11  
