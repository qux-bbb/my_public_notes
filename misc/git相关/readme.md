# git相关

git是Linus开发的开源代码版本控制工具。  
这里简单记自己会用到的命令和操作，系统的学习可以参考该链接：  
https://git-scm.com/book/zh/v2    

注意：做不确定的操作前记得先commit一下或者另外保存一份，不然教训惨痛  


## 名字含义
https://github.com/git/git/blob/e83c5163316f89bfbde7d9ab23ca2e25604af290/README  
```r
	GIT - the stupid content tracker

"git" can mean anything, depending on your mood.

 - random three-letter combination that is pronounceable, and not
   actually used by any common UNIX command.  The fact that it is a
   mispronounciation of "get" may or may not be relevant.
 - stupid. contemptible and despicable. simple. Take your pick from the
   dictionary of slang.
 - "global information tracker": you're in a good mood, and it actually
   works for you. Angels sing, and a light suddenly fills the room. 
 - "goddamn idiotic truckload of sh*t": when it breaks
```


## 创建代码仓库
```r
git init
```


## 删除本地仓库
删除文件夹即可  


## 查看当前配置
```r
git config --list
```


## 设置身份
右键打开Git Bash  
```r
git config user.name "Tony"
git config user.email "tony@email.com"
```
如果要设置全局，添加 `--global` 选项即可，不加 `--global` 就是只设置该仓库的身份  
去掉最后的名字和邮箱可用来查看信息  

取消设置 user.name  
```r
git config --unset user.name
```

如果发现有2对user.name和user.email，应该上面是全局的，下面是当前仓库的  


## 提交代码
```r
# 添加提交代码，a可以是文件，文件夹
git add a
# 添加所有文件
git add .
# 正式提交  -m 参数后的字符串表示描述信息，必须要有
# 如果想写多行，先只写开始的引号，然后就能回车了，最后补上结尾的引号即可
# 多行的时候，第一行做消息头，然后空一行，后面的做消息体
git commit -m "First commit"
```


## 查看修改内容
```r
# 查看文件修改情况
git status 
# 查看更改内容
git diff  
# 查看特定文件的更改内容
git diff src/..../MainActivity.java  
# 上一次和当前的区别 写法1
git diff HEAD^ HEAD 
# 上一次和当前的区别 写法2
git diff HEAD~1 HEAD 

# 查看暂存区(执行过add命令)与上一次commit的区别
git diff --staged

# 只显示内容不同的文件名
git diff --name-only
```


## 删除新生成的文件和文件夹
```r
git clean -df
```


## 撤销未提交的修改
1. 没有执行过add命令的文件
    ```r
    # 撤销单个文件
    git checkout src/....../MainActivity.java
    # 放弃所有修改 方法1
    git checkout .
    # 放弃所有修改 方法2
    git reset --hard
    ```
2. 执行过add命令的文件(就是撤销add)
    ```r
    git reset HEAD src/....../MainActivity.java
    ```
    然后按没执行add命令的文件处理  


## 撤销已提交(commit)的修改
```r
git reset HEAD^
```


## 查看提交记录
```r
# 查看全部提交记录
git log
# 查看其中一条记录 -1 表示只输出一行
git log 21d0cdf3afee1a7a783ba13b4e90f00295230b49 -1 
# 查看具体修改内容，因为有 -p
git log 21d0 -1 -p 

# 显示某次提交的修改
git show 某个提交编号
# 显示指定文件的修改记录
git log -p 文件名
```

## 强制恢复到某次提交
```r
git reset --hard 4458e09
```


## 从所有的提交记录中彻底删除一个文件
```r
git filter-branch --tree-filter 'rm top/secret/file' HEAD
```


## 删除某次提交记录
找到要删除的提交记录的前一条记录，假设为 abcd，执行命令  
```r
git rebase -i abcd
```
编辑，将想要删除的记录前的"pick"改为"drop"即可(如果想保存当前状态的所有文件，建议先保存一份，在删完某次提交记录后，重新复制回来，加一次commint)  
修改完成后，如果要同步到远程地址，需要强制push  
```r
git push --force
```


## 恢复删除的提交记录
查看历史记录  
```r
git reflog
```
复制要恢复阶段 的 hash值，执行reset命令  
```r
git reset --hard 4458e09
```


## 修改某次提交的commit内容
找到要修改的提交记录的前一条记录，假设为 abcd，执行命令  
```r
git rebase -i abcd
```
编辑，将想要修改的记录前的"pick"改为"edit"即可,wq保存退出，执行命令  
```r
git commit --amend
```
即可修改commit内容，修改完成后，wq保存退出，执行命令  
```r
git rebase --continue
```
即可修改完成，完成后，强制push到远程仓库  
```r
git push --force
```


## 暂时储藏修改的代码
```r
git stash
# -m 可添加说明
git stash -m "hello"
# 恢复
git stash pop
```
当pull出现冲突时，可以先stash，pull之后再pop，手动解决冲突，然后再提交代码  


## 忽略文件的文件名
`.gitignore` 在该文件中写不想git记录的文件名和文件夹就好了  


## 文件重命名
```r
git mv a.txt b.txt
```


## 分支
```r
# 查看当前版本库中有哪些分支
git branch -a
# 创建一个分支 version1.0
git branch version1.0
# 切换分支到 version1.0
git checkout version1.0

# 当前分支在master分支上，把在version1.0分支上修改并提交的内容合并到master分支上（有可能出现代码冲突，需手动解决冲突）
git merge version1.0
# 删除分支  version1.0
git branch -D version1.0
```


## 远程版本库协作
```r
# 将远程版本库的代码下载到本地
git clone https://github.com/example/test.git
# 将远程版本库的代码下载到本地，包含子仓库
git clone --recursive https://github.com/example/test.git
# 将本地代码同步到远程版本库，默认为`origin master`，可省略
# 添加 `--force` 选项可强制覆盖，不推荐
git push origin master
```


## 将远程版本库的修改同步到本地
```r
# 将远程版本库的代码同步到本地，存放到一个origin/master分支上
git fetch origin master
# 相当于执行fetch和merge这两个命令，可以从远程版本库获取最新的代码并且合并到本地
git pull origin master
# 拉取git子仓库
git pull origin master --recurse-submodules
```


## 只下载一个指定的分支
```r
git clone -b branch_name --single-branch https://github.com/example/test.git
```


## 代理
有时候`git clone`比较慢，加个代理  
```r
# 设置代理
git config --global http.proxy http://127.0.0.1:10809
git config --global https.proxy http://127.0.0.1:10809

# 取消代理
git config --global --unset http.proxy
git config --global --unset https.proxy

# 查看是否设置代理
git config --get http.proxy
git config --get https.proxy
```
github的地址虽然看起来是https，我设置了http才生效  
去掉 `--global` 选项就是设置单个项目的代理  


## 将本地git仓库传到github或gitlab或其它的位置
想要的效果是保留以前的提交记录  
先在github或gitlab创建一个同名空仓库  
然后本地用以下命令添加远程仓库就好，然后就可以像正常情况一样操作了  
```r
git remote add origin https://github.com/the_user/hello
```
第一次运行push指令应该这样：  
```r
git push --set-upstream origin master
```


## 更新远程仓库地址
```r
git config remote.origin.url git://new.url/proj.git
```
设置成git协议可以用公私钥体系获取和更新私有仓库  


## 创建命令别名
设置checkout别名为co  
```r
git config --global alias.co checkout
```
显示当前所有别名  
```r
git config --global --get-regexp alias
```


## 跟踪空文件夹
git不跟踪空文件夹，解决办法是在空文件夹里建一个空文件  


## 命令行显示汉字
部分情况下命令行执行结果的中文显示为8进制串，这样设置可以显示为中文：  
```r
git config --global core.quotepath false
```


## 参考链接
1. https://blog.csdn.net/wq6ylg08/article/details/88798254  
2. https://blog.csdn.net/logan_lg/article/details/81531796  
3. http://www-cs-students.stanford.edu/~blynn/gitmagic/intl/zh_cn/index.html  
4. https://baijiahao.baidu.com/s?id=1606573801465636505  
5. https://blog.csdn.net/u012145252/article/details/81775362  
