下载安装git-scm：https://git-scm.com/download/win  
打开git bash，执行以下命令，一路回车，生成公私钥对：  
```
ssh-keygen
```
根据提示找到该文件：`.ssh/id_rsa.pub`，这里可以把.ssh文件夹备份到其他位置  

访问该地址：https://gitee.com/profile/sshkeys， 添加刚生成的公钥内容  

在gitee创建新仓库，假设远程仓库地址为：`git@gitee.com:my_name/my-repository-name.git`  

在本地创建仓库并做第一次提交  
```
mkdir hello
cd hello
git init
echo "This is a README" > README.md
git add .
git commit -m "init"
```

设置远程仓库地址
```
git remote add origin git@gitee.com:my_name/my-repository-name.git
```

将本地仓库推送到远程
```
git push
```
第1次推送应该需要执行如下命令：  
```
git push --set-upstream origin master
```


参考链接：https://blog.csdn.net/feinifi/article/details/71169885  