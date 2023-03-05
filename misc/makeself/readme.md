# makeself

makeself, 在Unix上制作可自提取的存档。  

网站: https://makeself.io/  
github地址: https://github.com/megastep/makeself  

下载安装：  
在github的release页面下载.run文件执行即可  

用法：  
```r
makeself.sh [args] archive_dir file_name label startup_script [script_args]
```

官方示例：  
```r
makeself.sh /home/joe/mysoft mysoft.sh "Joe's Nice Software Package" ./setup
makeself.sh --notemp makeself makeself.run "Makeself by Stephane Peter" echo "Makeself has extracted itself"
```


## 简单示例
目录结构：  
```r
test_folder/
└── test.sh
```

test.sh内容：  
```bash
#!/bin/bash
while true
do
    echo "Hello World!"
    sleep 3
done
```

打包命令：  
```r
./makeself.sh /home/hello/Desktop/test_folder pack_test.sh "Just a description" ./test.sh
```

生成pack_test.sh之后执行就可以运行test.sh了  


## 提取文件
使用makeself生成的文件接受一些参数，所以可以通过这个命令来提取文件：  
```r
./pack_test.sh --noexec --keep
# 参数含义：
# --noexec  提取后不执行脚本，包含了`--noexec-cleanup`
# --keep    保留提取的文件
```

如果提取有问题的话，可以尝试手动提取：  
找到明文差不多最后的 b'exit $res\x0A` 之后就是被打包的文件了，可能是压缩包什么的，可以根据开头的hash验证  


---
2023/2/13  
