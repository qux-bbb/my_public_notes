# PE---导入表和hint

Hint: 本函数在其所驻留DLL的输出表中的序号。该域被PE装载器用来在DLL的输出表里快速查询函数。该值不是必需的，一些链接器将它设为0。  

经过测试，随意修改hint值，PE装载器仍然能够正确找到对应的函数  

记住一个重要的顺序：二进制顺序。如果按函数名导入，除去hint影响，PE装载器会按二进制顺序查找函数，hint不对也没关系  


二进制顺序的举例：  
```r
GoodMorning，GoodAfternoon，GoodEvening，HelloWorld
按二进制顺序排序为：
    GoodAfternoon
    GoodEvening
    GoodMorning
    HelloWorld
```


2020/3/31  
