# SEMA

github地址: https://github.com/csvl/SEMA  
官方文档: https://csvl.github.io/SEMA/  

SEMA, ToolChain using Symbolic Execution for Malware Analysis.  

安装方法：  
```bash
# 提前安装 git、make
# 安装docker，设置非root用户管理docker
# 如果docker网络不好，安装v2raya
git clone https://github.com/csvl/SEMA.git
cd SEMA/sema_toolchain
make run-toolchain
```

安装出错，应该是docker镜像内部的问题，不知道怎么解决：  
```r
Package apt-utils is not available, but is referred to by another package.
This may mean that the package is missing, has been obsoleted, or
is only available from another source
However the following packages replace it:
  apt

E: Package 'apt-utils' has no installation candidate
The command '/bin/sh -c apt-get --fix-missing install -y apt-utils' returned a non-zero code: 100
make: *** [Makefile:3: build-toolchain] Error 100
```


原始信息来源: https://mp.weixin.qq.com/s/1iViyl4zqYTuL12CdC1RSQ  


2024/10/3  
