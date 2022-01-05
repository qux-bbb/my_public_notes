# cargo设置源

cargo默认源在国内有时候可能很慢，可以设置一下使用国内源。  

创建 `~/.cargo/config` 文件，写入以下内容保存即可：  
```r
[source.crates-io]
registry = "https://github.com/rust-lang/crates.io-index"
replace-with = 'ustc'
[source.ustc]
registry = "git://mirrors.ustc.edu.cn/crates.io-index"
# 如果所处的环境中不允许使用 git 协议，可以把上面的地址改为
# registry = "https://mirrors.ustc.edu.cn/crates.io-index"
#[http]
#check-revoke = false
```


原链接: https://www.cnblogs.com/qumogu/p/14167597.html  


2022/1/5  
