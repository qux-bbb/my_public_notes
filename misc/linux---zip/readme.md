# linux---zip

ubuntu安装命令：  
```bash
sudo apt install zip
```  

压缩文件：
```bash 
# 将file1、file2压缩到all.zip中
zip all.zip file1 file2

# 将非空文件夹递归压缩到folder.zip中
zip -r folder.zip my_folder

# -e选项可以设置密码
```

解压缩：  
```bash
unzip a.zip
```

查看压缩文件：  
```bash
unzip -v a.zip
```

解压缩压缩包中指定文件:  
```bash
unzip a.zip b_folder/c.txt
```

解压时使用密码(直接unzip可根据提示输入密码，不建议使用-P选项)：  
```bash
unzip -r -P infected folder.zip my_folder
```
