# logicdata文件

做题的时候碰到了后缀是logicdata的文件，是IC卡片(集成电路)的交互数据  

可以从这里下载软件打开分析: https://www.saleae.com/downloads/  
遇到的题目是1.x版本才能打开的: https://support.saleae.com/logic-software/legacy-software/older-software-releases  
程序预置了一些类型的分析器，如果有合适的，可以选择进行分析  
右上角点"Option"可以选择导出csv文件，方便脚本解析数据  

这个软件也可以生成logicdata文件  

一些卡片的pdf文档，可以在这里搜索下载: https://datasheetspdf.com/datasheet/  
比如4442卡的说明文档: https://datasheetspdf.com/datasheet/SLE4442.html  

这里有一个题目例子和题解: https://github.com/EmpireCTF/empirectf/blob/master/writeups/2018-06-19-SCTF/README.md#434-misc--神秘的交易  
这是解析导出csv数据的python脚本: [parser.py](files/parser.py), 有2个地方没找到对应逻辑，但去掉对结果也没什么影响  


2021/9/8  
