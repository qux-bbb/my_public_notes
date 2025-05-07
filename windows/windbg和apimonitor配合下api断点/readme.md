# windbg和apimonitor配合下api断点

apimonitor可以很轻松地抓到api调用，然后就可以在windbg里下api断点

比如api名字是world，相关的dll是hello.dll，在windbg里下断点的命令就是：  
```r
bp hello!world
```


2020/7/15  
