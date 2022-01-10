# powershell反混淆记录

```r
$shellid[1]+$shellid[13]+'x'  =  'iex'
`$pshome[4]+`$pshome[34]+'X'  =  'iex'
"\" +  ([char]44).tostring() + "\"  =  ,  # 不确定
"\" = "  # 不确定
```
上面的这些，等号前面的都可以直接粘到powershell命令行，回车就能看到实际的字符串了  
小括号里有字符串的，也可以做类似操作  

`${a}` 等价于 `$a`，指的是一个变量  
`.("Get-Alias")` 等价于 `Get-Alias`，都是获取命令别名  

反引号"`"用作转义，有意义的反义如下，其它没什么用，可以直接删掉  
```r
`0    Null
`a    Alert
`b    Backspace
`f    Form feed
`n    New line
`r    Carriage return
`t    Horizontal tab
`v    Vertical tab
```

竖线就是管道符，前后可分别处理  
一般来说，管道符最后是 "iex" 或者是变形的东西，可以直接把这个管道符和最后的内容删掉，这样之后执行脚本，可以直接输出上一层脚本内容  

powershell不区分大小写，有时候可以直接全部转成小写，方便查看（有时候如果内容和大小写有关，那就不能这么做了）  

相关资料：  
https://bbs.pediy.com/thread-248034.htm  


2019/11/27  
