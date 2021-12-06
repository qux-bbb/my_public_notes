# 删除GNU GRUB菜单

想给移动硬盘装ubuntu系统，在自己的windows上关机选择U盘启动，把ubuntu装到了移动硬盘里，拔掉移动硬盘，启动自己的windows，发现有了一个新的菜单，输入exit 回车才能进入windows。新的菜单如下：  
```r
                                    GNU GRUB version 2.04

Minimal BASH-like line editing is supported. For the first word, TAB lists possible
command completions. Anywhere else TAB lists possible device or file completions.

grub> _
```

在Ask Ubuntu找到了好的解决方法，记录如下：  
1. Run a `cmd.exe` process with administrator privileges
2. Run `diskpart`
3. Type: `list disk` then `sel disk X` where X is the drive your boot files reside on
4. Type `list vol` to see all partitions (volumes) on the disk (the EFI volume will be formatted in FAT, others will be NTFS)
5. Select the EFI volume by typing: `sel vol Y` where Y is the `SYSTEM` volume (this is almost always the EFI partition)
6. For convenience, assign a drive letter by typing: `assign letter=Z:` where Z is a free (unused) drive letter
7. Type `exit` to leave disk part
8. While still in the `cmd` prompt, type: `Z:` and hit enter, where Z was the drive letter you just created.
9. Type `dir` to list directories on this mounted EFI partition
10. If you are in the right place, you should see a directory called `EFI`
11. Type `cd EFI` and then `dir` to list the child directories inside `EFI`
12. Type `rmdir /S ubuntu` to delete the ubuntu boot directory

所以如果想单独装系统，就把别的硬盘给去掉。  


原链接：https://askubuntu.com/questions/429610/uninstall-grub-and-use-windows-bootloader  


2020/12/16  
