# windbg和apimonitor配合下api断点

apimonitor 可以很轻松地抓到 api 调用，如果想把 apimonitor 抓到的 api 在 windbg 里下 api 断点，应该怎么做呢？  

**下面的做法是傻子，因为在 apimonitor里有对应的dll名称**  

比如 api 名字是 world，在 apimonitor 左侧确定相关的 dll 是 hello.dll，在 windbg 里下断点的命令就是：  
```r
bp hello!world
```


2020/7/15  
