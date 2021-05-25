# github---下载部分文件或文件夹

第1种方法还是太慢，先用第2种方法  

## 方法1
```bash
# 初始化本地仓库
mkdir tmp_folder && cd tmp_folder
git init
# 设置远程仓库地址
git remote add -f origin https://github.com/seabluescn/ML_BinaryClassification.git
# 启用过滤功能
git config core.sparsecheckout true
# 将BinaryClassification_Beauty这个关键字加入过滤列表
# 如果有其它关键字可以多次运行该命令或者直接编辑相应文件
# 关键字是文件夹或文件皆可
echo BinaryClassification_Beauty >> .git/info/sparse-checkout
# 拉取代码
git pull origin master
```

参考: https://www.cnblogs.com/seabluescn/p/10613167.html  


## 方法2
要有svn，假如文件夹为 https://github.com/qux-bbb/CTF_wp/tree/master/ABCTF-2016_writeup  
将 tree/master 替换为 trunk  
`svn checkout https://github.com/qux-bbb/CTF_wp/trunk/ABCTF-2016_writeup`  


2020/3/19  
