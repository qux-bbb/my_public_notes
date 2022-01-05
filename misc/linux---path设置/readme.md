# linux---path设置

`$PATH` 类似windows环境变量的path。  
`PATH` 是在 `/etc/environment` 文件中设定的，一般不应该修改该文件。  

## 输出PATH
```sh
echo $PATH
```

## 临时设置
单个终端窗口中修改，在此窗口即时生效，关闭窗口即失效：  
```sh
export PATH=$PATH:/place/with/the/file
```

## 针对某个用户的path
修改文件: `~/.profile`  
如果shell是bash, 还可以修改`~/.bashrc` `~/.bash_profile`  

## 修改到系统path
将`export PATH=$PATH:/place/with/the/file` 放到`/etc/profile`文件的最后  


## 参考链接
1. https://opensource.com/article/17/6/set-path-linux  
2. https://www.fujieace.com/linux/path-2.html  


2020/2/26  
