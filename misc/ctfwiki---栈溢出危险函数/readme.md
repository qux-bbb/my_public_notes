# ctfwiki---栈溢出危险函数

输入  
- gets，直接读取一行，忽略'\x00'
- scanf
- vscanf

输出  
- sprintf

字符串  
- strcpy，字符串复制，遇到'\x00'停止
- strcat，字符串拼接，遇到'\x00'停止
- bcopy


2020/6/29  
