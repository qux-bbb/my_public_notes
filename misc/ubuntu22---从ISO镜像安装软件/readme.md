# ubuntu22---从ISO镜像安装软件

没网的时候，可以从ISO镜像安装一些软件  

```
挂载ISO镜像  

Settings -> About -> Software Updates 
勾选"Installable from CD-ROM/DVD"下的"Installation medium with..."，其它全部取消勾选  

编辑 /etc/apt/source.list (可以先备份一下), 除了"deb cdrom:..."一行，其它全部"#"注释

apt update
```

这样之后，就可以装软件了，只是软件不多，试了可以装 vim, 不能装 openssh-server, samba, 所以并没有什么用    


2023/6/11  
