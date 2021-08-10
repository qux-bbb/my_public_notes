# linux---path设置

## 输出PATH
```sh
echo $PATH
```

## 临时设置
```sh
export PATH=$PATH:/place/with/the/file
```

## 修改到系统path
将`export PATH=$PATH:/place/with/the/file` 放到`/etc/profile`文件的最后  

## 针对某个用户的path
也是修改文件: `~/.profile`  
如果shell是bash, 还可以修改`~/.bashrc` `~/.bash_profile`  

## 参考链接
1. https://opensource.com/article/17/6/set-path-linux  
2. https://www.fujieace.com/linux/path-2.html  


2020/2/26  
