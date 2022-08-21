# pdf相关了解

pdf, Portable Document Format, 便携式文档格式  

pdf的解析很容易懂, 这里举一个明文的例子:  
```r
%PDF-1.7

1 0 obj  % entry point
<<
  /Type /Catalog
  /Pages 2 0 R
>>
endobj

2 0 obj
<<
  /Type /Pages
  /MediaBox [ 0 0 200 200 ]
  /Count 1
  /Kids [ 3 0 R ]
>>
endobj

3 0 obj
<<
  /Type /Page
  /Parent 2 0 R
  /Resources <<
    /Font <<
      /F1 4 0 R 
    >>
  >>
  /Contents 5 0 R
>>
endobj

4 0 obj
<<
  /Type /Font
  /Subtype /Type1
  /BaseFont /Times-Roman
>>
endobj

5 0 obj  % page content
<<
  /Length 44
>>
stream
BT
70 50 TD
/F1 12 Tf
(Hello, world!) Tj
ET
endstream
endobj

xref
0 6
0000000000 65535 f 
0000000010 00000 n 
0000000079 00000 n 
0000000173 00000 n 
0000000301 00000 n 
0000000380 00000 n 
trailer
<<
  /Size 6
  /Root 1 0 R
>>
startxref
492
%%EOF
```

这里所有的数字都是十进制的  
针对这个例子, 如果保存到文件查看, 注意换行使用`LF`而不是`CRLF`, 用前者才能有正确的偏移  

解析大概过程:  
首先判断头尾是否为PDF, 即`%PDF*`, `%%EOF`  
然后根据倒数第3第2行指出的偏移找到xref表起始位置, 开始一个个节点的解析  
xref表中每一项不是按先后顺序来的, 是按序号排列的  

`%`用作注释符  


参考链接:  
1. https://blog.csdn.net/P876643136/article/details/79449060  
2. https://www.jianshu.com/p/f48cc9077c10  
3. https://web.archive.org/web/20141010035745/http://gnupdf.org/Introduction_to_PDF 翻墙才能看  
4. https://www.adobe.com/content/dam/acom/en/devnet/acrobat/pdfs/PDF32000_2008.pdf  


---
2020/1/14  
