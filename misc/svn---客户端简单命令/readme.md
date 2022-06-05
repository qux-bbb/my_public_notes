# svn---客户端简单命令

```sh
# 检出，将指定的库中代码检出到当前目录，简写为 svn co
svn checkout svn://192.168.0.1/runoob01

# 查看更改
svn diff

# 只显示被修改文件名
svn diff --summarize

# 查看一个文件不同版本的差异
svn diff -r 1:2 hello.py

# 查看当前状态
svn status

# 添加文件到版本控制中
svn add readme.txt

# 提交更改, -m 为注释信息，为本次提交添加说明
svn commit -m "一次提交"

# 查看历史信息，-v可以列出涉及文件
svn log

# 列出远程仓库目录
svn list <远程仓库地址>
```

注意：  
commit 之前一定要 update，不然直接盖掉别人的代码就很尴尬  


参考:  
1. http://www.runoob.com/svn/svn-tutorial.html
2. https://blog.csdn.net/mandagod/article/details/54141696


2018/10/29  
