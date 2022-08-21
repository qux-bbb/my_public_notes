# pdf简介

写在最前面：  
gnupdf 已经不存在了，不过这篇文章对 pdf 结构的介绍还是很好的。  

原链接： https://web.archive.org/web/20141010035745/http://gnupdf.org/Introduction_to_PDF  

# PDF 简介
PDF，Portable Format Document，可移植格式文档。这种格式意味着在所有平台和媒介（屏幕，打印机...）上显示完全一致的内容。  

- [pdf简介](#pdf简介)
- [PDF 简介](#pdf-简介)
  - [一个例子](#一个例子)
  - [一般结构](#一般结构)
    - [对象语法](#对象语法)
    - [交叉引用表](#交叉引用表)
    - [注释](#注释)
  - [如何解析这个文件](#如何解析这个文件)
  - [筛选器](#筛选器)
  - [参考资料](#参考资料)
  - [TODO](#todo)

## 一个例子
我们从一个非常简单的 "Hello，world!" PDF 开始。你可以复制/粘贴到文本编辑器中（换行用 "LF"），将其另存为hello.pdf，或者从这里下载：[File:Hello.pdf](https://web.archive.org/web/20141010035745/http://gnupdf.org/File:Hello.pdf)。使用 xpdf 或 Evince 等 [PDF 阅读器](https://web.archive.org/web/20141010035745/http://www.pdfreaders.org/) 打开它：  
![pdf image][ceaf9cae3eddfed0cbe29e2e2323dc44]  
```
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

本 PDF 是手动编写的，出于介绍的目的进行了简化。实际的 PDF 通常更复杂。  
练习 1：用 OpenOffice.org 写一个 "Hello, world!" 文档并将其导出为PDF。和 hello.pdf 比较。  
注意：如果使用命令行工具 less 查看 PDF ，你可能需要添加 -L 选项（该选项将禁用默认运行 pdftotext 的输入预处理器，pdftotext 的处理会屏蔽原始文件内容）。  


## 一般结构
如我们所见，该文档具有基于文本的常规结构，这样研究起来是很方便的。不过，PDF 文件通常会包含非 ASCII（"二进制"）数据，一般都应该把PDF当做二进制文件。  
一个简单的 PDF 包含 4 个部分：  
- 头，表示 PDF 版本（以及用于指定 PDF 是否包含二进制数据的可选行）  
```
%PDF-1.7
```
- 主体，包含文档中使用的一系列对象  
```
1 0 obj
...
endobj
2 0 obj
...
endobj
...
```
- 交叉引用表，用于指定对象的位置  
```
xref
0 6
0000000000 65535 f 
0000000010 00000 n 
0000000079 00000 n 
0000000173 00000 n 
0000000301 00000 n 
0000000380 00000 n 
```
- trailer，其中包含有关文档起始位置的信息（直译是预告片，感觉不太合适）  
```
trailer
<<
  /Size 6
  /Root 1 0 R
>>
startxref
492
%%EOF
```

在完整的文档结构中，可以附加其他 body + cross-reference + trailer 元素来完善现有文档，但是在我们的示例中不会看到这种情况。  


### 对象语法
在主体（对象列表）中，我们可以看到各种定义：  
- [间接对象](https://web.archive.org/web/20141010035745/http://gnupdf.org/Indirect_Object)​​（1 0 obj ... endojb）：定义一个有编号的顶级对象。第一个数字（1）是对象编号，第二个数字（0）是修订版本编号，我们在此示例中不使用。  

有9种类型的对象：  
- [数字](https://web.archive.org/web/20141010035745/http://gnupdf.org/Number)：比如 3  
- [间接引用](https://web.archive.org/web/20141010035745/http://gnupdf.org/Indirect_Object)（n r R）：引用对象，例如 5 0 R。如果对象不存在，则等效于 Null 对象（参见下文）。  
- [名称](https://web.archive.org/web/20141010035745/http://gnupdf.org/Name)（/Name）：名称是标识符。类似 Lisp 或 Scheme 中的单引号特殊形式（例如 'ok）。开头的 / 引入名称，但不属于名称；这类似于 Bash，Perl 或 PHP 中的 $。  
- [字典](https://web.archive.org/web/20141010035745/http://gnupdf.org/Dictionary)（<< ... >>）：（Name，Object）对的无序列表。本质上是哈希表。对象部分可以是另一个名称（例如 /Type /Font）。  
- [数组](https://web.archive.org/web/20141010035745/http://gnupdf.org/Array)（[x y z ...]）：对象的有序列表，例如 [0 0 200 200]。  
- [字符串对象](https://web.archive.org/web/20141010035745/http://gnupdf.org/String_Object)（（text））：文本。完整的语法很复杂，但是现在只需关注括号之间的文本即可，例如 (Hello, world!)。  
- [流](https://web.archive.org/web/20141010035745/http://gnupdf.org/Stream)（<< /Length ... >> stream ... endstream）：嵌入式数据，可以压缩。它以描述流的字典开始，该字典描述流的长度或使用的编码（/Filter）。  

还有在此示例中未使用的：  
- [布尔值](https://web.archive.org/web/20141010035745/http://gnupdf.org/Boolean)：对或错。  
- [空对象](https://web.archive.org/web/20141010035745/http://gnupdf.org/Null_Object)：null。  

表现和组织这些对象构成了 GNUpdf 库的对象层。  


### 交叉引用表
```
xref
0 6
0000000000 65535 f 
0000000010 00000 n 
0000000079 00000 n 
0000000173 00000 n 
0000000301 00000 n 
0000000380 00000 n 
```

交叉引用表就是对象的顺序列表（＃2，＃3，＃4 ...），更确切地说是对象偏移量（距文件开头的字节位置）。交叉引用表允许按其编号轻松快速地访问任何给定对象。而 HTML 恰好相反，HTML 纯粹是顺序的并且不能很好地处理大型文档。  
前两个数字表示“我将引入6个对象偏移，从0开始计数”。  
每行包含对象定义的偏移量，修订号（此处未使用）和开/关标记 f（free，空闲）或 n（in use，正在使用）。  
现在我们可以先忽略第一个偏移量。  
解释下面的含义：  
- 对象 ＃1 的偏移量为 10 
- 对象 ＃2 的偏移量为 79 
- ... 
- 对象 ＃5 偏移 380

如果你修改了测试文档，要记住更新所有这些偏移量以及描述 xref 偏移量的 startxref 行。  
交叉引用表还可以包含更复杂的声明，我们将在后面介绍。  


### 注释
```
% page content
```
注释以百分比（％）字符开头，并在下一个换行符处结束。从效果来讲，注释等效于空格字符，并且不包括结尾的换行符。  


## 如何解析这个文件
PDF阅读器不会按顺序（从上到下）分析文档，而是以更复杂的方式访问文件：  
- 首先，读取第一行以获取 PDF `版本`  
- 然后转到文档的末尾，检查 `%%EOF` 标记，再向上一行读取 492，这是交叉引用表的 `偏移量`（上一部分介绍过）。现在你就会明白为什么通常无法阅读尚未下载完成的大 PDF。当 trailer 缺失或损坏时，某些阅读器会尝试通过扫描整个文件来重建索引，但这要慢得多。  
- 如上所述，接着跳到交叉引用表并建立 `对象偏移量列表`。  
- 在交叉引用表之后，就可以读取 trailer 字典了，这里包含`Catalog`（意思是目录），即文档的开始。它是通过一个指向对象 1 的间接引用：1 0 R 来指定的。  

到目前为止，阅读器可以随机（非顺序）访问 PDF 文件，并获取文档的整体结构。  
- 接下来检查 `Catalog` 对象。在我们的例子里，它仅包含对 `Pages` 对象（编号2）的引用。  
- Pages 对象是 `树状` 数据结构。它是一个节点，可以引用叶子（pages）或其他节点（它们本身可以引用叶子和节点）。在我们的例子里，Pages 对象仅引用了 1 个 Page（/Count 1），该页面在 Kids 列表中指定，包含对对象 3：3 0 R 的间接引用。Pages 对象还定义了存放子对象的介质的大小，该大小由 Page（叶）对象继承，可以重新定义。在这里，我们定义了一个 200x200 的小盒子。  
- `Page` 对象引用其父对象（/Parent 2 0 R），呈现页面所需的一组资源（此处是字体，对象 4）及其实际内容（对象 5）。  
- 对象 4 是字体定义。为了简单起见，这里我们使用的是 14 种基本字体之一（Times-Roman）。  
- 对象 5 是一个 `流` 对象，其中包含呈现页面的指令。这些指令与本文档的其余部分有很大不同，完全可以视为另一种语言。在BT 和 ET 之间，指令描述了 3 个操作。它们使用了后缀运算符，这是 PDF 的前身 PostScript 的缩影。  
    - 位置 - 70 50 TD：应用 TD 运算符，它将文本光标放在页面上，带有参数 70 和 50，表示（x, y）坐标。默认情况下，光标位于页面的左下角（0, 0）。因此（70, 50）表示“向上 70 个单位”和“向右 50 个单位”。这与 2D 图形编程不同，后者通常将y轴反转。这里是经典的数学/几何坐标系。  
    - 字体 - /F1 12 Tf：应用 Tf 运算符，该运算符设置字体名称和字体大小。如资源中所定义，字体为 F1，大小为 12。字体是必须指定的，因为没有默认字体。  
    - 文本显示-(Hello, world!) Tj：应用 Tj 运算符，该运算符用于显示文本，这里显示的文本字符串是 Hello, world!。  

大功告成！  


## 筛选器
我们例子中的 `流` 直接表示为明文。实际上这并不常见，大多数流都经过压缩，其内容（在 stream 和 endstream 之间）是二进制数据。  
本部分的目标是将 PDF 中的纯文本流替换为压缩流，可以在这里查看结果： [File:Hello-stream.pdf](https://web.archive.org/web/20141010035745/http://gnupdf.org/File:Hello-stream.pdf)。  
要编码或解码流，可以使用 GNUpdf 的 pdf-filter 组件。  
尝试用一下 FlateDecode 过滤器：  
```
# Encode
$ ./pdf-filter --flateenc <<EOF > filtered.bin
BT
70 50 TD
/F1 12 Tf
(Hello, world!) Tj
ET
EOF

# Check size:
$ ls -l filtered.bin 
-rw-r--r-- 1 me me 52 Jan 26 23:59 filtered.bin
# It's binary:
$ file filtered.bin 
filtered.bin: data

# Decode it back:
./pdf-filter --flatedec < filtered.bin
BT
70 50 TD
/F1 12 Tf
(Hello, world!) Tj
ET
```
注意：如果从现有的 PDF 复制/粘贴流以进行解码，请确保没有编码问题。验证一下你提取的流文件（上面的 filtered.bin）具有与 /Length 中指定的大小相同的大小。如果你使用 Emacs，请尝试在缓冲区之间进行复制/粘贴之前尝试使用  raw-text 编码（使用 M-x set-buffer-file-coding-system 或 C-x RET f）。  

这是对象 5 的新版本（"Hello, world!"  的文本显示）：  
```
5 0 obj  % page content
<<
  /Length 52
  /Filter /FlateDecode
>>
stream
xs
á27P05P�qáÒw3T04R�IãÒðHÍÉÉ×Q(Ï/ÊIQÔT�Éâr
á�á·
Á
endstream
endobj
```
- 注意：由于流非常短，因此压缩版本实际上比未压缩版本长！ 
- 注意：请勿尝试从此页面复制/粘贴它，不支持这样操作二进制数据。

由于我们要在文件中引入非 ASCII 内容，因此 PDF 格式要求我们添加至少4个以注释符开头的二进制字符（ASCII值 >= 128），以便通用工具可以将其检测为二进制文件：  
```
%PDF-1.7
%éééé
```

最好使用 [128, 159] 中的字符，这些字符不是 ASCII 或 Latin-1 的一部分。不过，这不一定奏效，因为 diff（1）和 [mercurial](https://web.archive.org/web/20141010035745/http://www.selenic.com/mercurial/wiki/index.cgi/BinaryFiles) 之类的程序仅在文件包含 NUL（0）字符时才将其视为二进制文件。  

我们还需要更新交叉引用表和 startxref 中的偏移量：  
```
xref
0 6
0000000000 65535 f 
0000000016 00000 n 
0000000085 00000 n 
0000000179 00000 n 
0000000307 00000 n 
0000000386 00000 n 
trailer
<<
  /Size 6
  /Root 1 0 R
>>
startxref
530
%%EOF
```

注意：要快速确定 Emacs 下文件中某个位置的偏移量，可以从文档的开头选择到该位置，使用 M-=（count-lines-region）命令 查看 "characters" 状态即可：  
```
Region has 52 lines, 530 characters
```

这里有更多的过滤器：  
- [Category:PDF_Filters](https://web.archive.org/web/20141010035745/http://gnupdf.org/Category:PDF_Filters)：过滤器列表 
- [Lib:Architecture/Base_Layer/Stream_Module](https://web.archive.org/web/20141010035745/http://gnupdf.org/Lib:Architecture/Base_Layer/Stream_Module)：由libgnupdf的Base层提供的流处理 

如果要研究现有的PDF，可以使用 [pdftk](https://web.archive.org/web/20141010035745/http://www.accesspdf.com/pdftk/) 工具的 uncompress 命令将所有压缩的流转换为明文：  
```
pdftk hello-stream.pdf output hello-clear.pdf uncompress
```


## 参考资料
PDF 最初是 Adobe 的专有格式，但自 2008 年以来，就成了 ISO-32000 标准（更确切地说是 ISO 32000-1:2008）。  
你可以从 ISO 花费 380 瑞士法郎（约250欧元）获得电子副本。Adobe发布的副本虽然不是官方的，但具有相同的技术内容和页码。  
- [Adobe - PDF Developer Center: PDF Reference](https://web.archive.org/web/20141010035745/http://www.adobe.com/devnet/pdf/pdf_reference.html)

要下载的是 "Document management – Portable document format – Part 1: PDF 1.7, First Edition (July, 2008)"。  
请注意，ISO-32000 是非免费文档，请勿在此 Wiki 上转载相关内容。位于 gnupdf.org 的 [PDF知识](https://web.archive.org/web/20141010035745/http://gnupdf.org/Category:PDF) 部分，旨在提供免费的 PDF 格式文档，你可以阅读，修改，共享和重新分发。  
你还可以看到一些扩展文档：这些是不属于 ISO-32000 的 PDF 特性，可能在该格式的下一个修订版中提出，也可能不会。保持 PDF 的开放标准是一场长期的战斗。  


## TODO
- 把“如何解析这个文件”章节描述更清晰一些。目前有点难理解。  
- 添加一张具有基本树结构（节点和叶子）的图片，可以很好地说明 /Pages 和 /Page 的区别。
- 说明 PDF/A 和 PDF/X 分别适用的地方（参阅 [Goals_and_Motivations](https://web.archive.org/web/20141010035745/http://gnupdf.org/Goals_and_Motivations)）  

[ceaf9cae3eddfed0cbe29e2e2323dc44]: data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAWAAAAE4CAIAAADq3r6BAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAArMSURBVHhe7dppqJVlv8fxbXOmPTmQ1c6IMiMsigahyCxfmJahFEU2UUkDdCAiCrJ8YdiAEFEdHuhF2UCjERWVYdk82AClzWSjmVOWRXOp55/3eja29befzqPHs4vP58Xyuu577du1XtzfdV1r7x5vzZ3TBrAum7T+BViLQADRhtxijBw1ujUCuoGZj81ojf5TGzgQCxYsaE2A/1ft7e3rHwhbDPjbqs/s9VzXCwQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCQQQCUQ3smLFit/WsHLlyjpYj635avWc5snrtGrVqrlz586fP3+d026l69e2fPny2bNntyZtbT/88MOrr77amrARCUQ38sILL5x88smbb775Fltscfnll3/00Ud1cOHChVOnTu3Vq1cdHzdu3MyZM5snr+25554bPXr0vvvuO2fOnLWn3UoXr+3XX3+t9ztgwIApU6a0DrW1TZ48eejQoW+++WZrzsYiEN3IYYcddt1119VgyJAhFYhBgwbVuL29feLEiYceemiN686p++r3p67LsGHDLrnkktZkrWm30sVrqw5efPHFu+66a2u+2pIlS+px8eLFzZSNRiC6l6222qoet9xyy2baoTleK4tmmnT6wbWv0310/doqE63RajvuuGM97rDDDs2UjUYg/qp++eWXJ5544t577/38889bh/6ElStXvvTSS3fddVct8n/77bfW0awu/tZq8+fP//7775tx+fLLLzvOLliwoHlySddftWrVG2+8UYPZs2fXqeZgJytWrHjmmWfqHTXrhTU1C4qBAwc2UzYagfhLqq37ueee+9VXX73//vu77777tGnTWie69OGHH9YuZt68eYMHD64f2Xvvvev2bp0LKgoHH3zwqFGj6g7fZJNNpk+fvs8++/zzn//cdNNN62wl4Mgjj+xY+afr1z1fP1UXufHGG4855pjhw4fXZZsf6bBo0aIRI0bUz+62226TJk3q9OVlvcd/rNaas7EIRHdUn8mX/dF7773XOtfW9uOPP55wwgnXXHNNPda9VPfVeeedt3z58tbpoG7msWPHjhs37tRTTz3ggANuuummAQMGjBkzpq7Wesa67LnnnhMmTKgS1c259dZbX3rppf379+/Ro0efPn3qbL9+/YYNG7b//vvXuIvr1+us63z99dd77bXXu+++e8cdd/Ts2XP15VuqPieeeOLRRx9d/9eBBx54ww03dNpMDRo0aJdddmlN2IgEojvq1avXoX/Ut2/f1rm2tkceeWTp0qWVhv9abdmyZbWwf+WVV1qng1mzZr399ttHHHFEM62b/Jxzzvn0008feOCB5khy1lln1U1eq4Aa131ba4HaQfz88881vfPOO0877bTVz/o31+/du3clptYX1Zfx48fX2eZpjdp31Oai4tJM63+puDTjRnt7e6evLdk4BKI7qnupFuRr2n777VvnVu8vasn93/9Safjpp59GjhzZOh00q/01v/xrPvnfeeedZpoMGTLkkEMOufnmm2tcO5q6e2st8PDDD9fH/qOPPlpbjOZp//b6tUNpBmt7/vnn63HN99jJZptt1lyNjUwg/npWrFhRe/Wu/2JqbbVBqMfPPvusmZZap3Q8dq0WEfUhX9uca6+99vrrrz/88MNvueWWl19+ubYDzZcRZX2u33wlUd1ppus0fPjw1oiNSCC6l/pYbo3+aM3je+yxx/Lly++7777WfPWtVXv+1iSoVUA9Pvvss820fPHFF/XYsSnowvHHH7/tttteffXV33333eDBgydMmDBjxowrr7zyzDPPbD1j/a5fC6J6fPLJJ5vpOv2Z67DBCUT30nxlWFuGZtphzeNjx47dbrvtaod/9913L1y4sNbnp59+erOBb5YVzd9od5rut99+xx57bH3yf/PNN6tPtk2fPr2ODB06tMZnnHFGfUSn35hus802p5xyyq233nr++efX9Ljjjqt1QW0Z2tvbmyeUrq9fr6HTb1XXfG31jvr37z958uRmAVIvoyxevLjjlx0PPfTQUUcdtXTp0mbKRiMQ3cjTTz99wQUX1KD27RMnTvzggw9qvGDBgvrofvHFF2t80UUX1ba/b9++999/f92i48eP32mnnS688MKpU6f269fv9ddfb/4Qc9q0aa+99lqnaQ1uu+22MWPGjB49um71yy67rO7k22+/vY6Xp556qj78u1iG1C5jxIgRBx10UI1rN3HSSSedffbZzakO6fr33HPPrFmzli1bdtVVV3388cd1pNNrq+XJgw8+2KNHj1qeVFCuuOKKel/1BjtWSRXBWrN88sknzZSNpsdbczfYH+qPHDV6zb+Z4f9UfSDPmzevZ8+eAwcO7PRLga7VfTt//vydd965liGtQ6tXKI8//viiRYvWvu071B1eGeoY9+nTZ53fO67z+n9G891K845qD7Xmj9ebXbJkSVWjNedP6FjfzXxsRjP4DwgEv/v2228nTZpUS5Xmu0b+BjZIIGwx+N2cOXOmTJmiDnQiEPxu2LBhvXv3bk3gXwQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiAQCiHq8NXdOa7jeRo4a3RoB3cbMx2a0Rv97G3IFUa9jfV4K0N3YYgDRhtxiAH8zVhBA0Nb2PyzMfWiMPkE4AAAAAElFTkSuQmCC


---
2020/6/11  
