# 旧电脑重装linux系统问题解决

keywords: 安装系统  

## 出现 1962 错误，操作系统未找到
这个应该是BIOS 和 UEFI 的设置出错了，在出现 `Foucus UEFI installation` 时，选择 No 选项  

## 出现开机只有一个光标闪的情况
我遇到的是因为GRUB引导没有装  

所以解决办法就是：在出现 `安装GRUB` 选项时，选择 Yes 选项  

## 如果选错了，怎么办
如果第一个选错了，麻烦点，做个PE盘（大白菜或者老毛桃），把分区全部删掉，再去重装系统吧（用里面的 DiskGenius）  

第二个选错可以重新来一遍，遇到GRUB安装，选择Yes 就好了  

## 创建文件系统失败
`failed to create a file system it says "the ext4 file system creation in partition #1 (0,0,0)(sda) failed.`  
按选错了的方法试一试  


---
2016/6/5  
