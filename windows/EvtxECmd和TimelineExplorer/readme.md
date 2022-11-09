# EvtxECmd和TimelineExplorer

keywords: 事件查看器 日志转换  

https://ericzimmerman.github.io/#!index.md  

主机导出Security.evtx类似的日志，通过EvtxECmd转换为csv文件，再用TimelineExplorer打开  
```r
EvtxECmd.exe -f Security.evtx --csv . --csvf result.csv
```

EvtxECmd 效果还不错，TimelineExplorer不怎么样，可以把生成的csv用excel打开查看，方便多了。  


感谢yrq  


2022/11/9  
