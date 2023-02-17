# makeself

makeself, 在Unix上制作可自提取的存档。  

网站: https://makeself.io/  
github地址: https://github.com/megastep/makeself  

用法：  
```r
makeself.sh [args] archive_dir file_name label startup_script [script_args]
```

示例：  
```r
makeself.sh /home/joe/mysoft mysoft.sh "Joe's Nice Software Package" ./setup
makeself.sh --notemp makeself makeself.run "Makeself by Stephane Peter" echo "Makeself has extracted itself"
```

如果想提取文件，找到明文差不多最后的 b'exit $res\x0A` 之后就是文件了，可能是压缩包什么的，可以根据开头的hash验证  


2023/2/13  
