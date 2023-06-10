# virtualenv构建虚拟环境安装w3af_gui

```r
$ cd w3af  
$ sudo apt-get install python-gtksourceview2 python-gtk2
$ sudo apt-get install graphviz
$ sudo apt-get build-dep python-lxml 
$ virtualenv --system-site-packages venv
$ . venv/bin/activate
(venv)$ ./w3af_gui
(venv)$ . /tmp/w3af_dependency_install.sh
```
上面命令执行完成之后，再 `./w3af_gui` 报错：`ImportError: No module named webkit`  
查询发现https://github.com/andresriancho/w3af/issues/14190  
执行以下命令可以解决问题：  
```r
wget http://ftp.cn.debian.org/debian/pool/main/p/python-support/python-support_1.0.15_all.deb
dpkg -i python-support_1.0.15_all.deb

wget http://ftp.cn.debian.org/debian/pool/main/p/pywebkitgtk/python-webkit_1.1.8-3_amd64.deb
dpkg -i python-webkit_1.1.8-3_amd64.deb

apt install python-gtk2-dev
wget http://ftp.cn.debian.org/debian/pool/main/p/pywebkitgtk/python-webkit-dev_1.1.8-3_all.deb
dpkg -i python-webkit-dev_1.1.8-3_all.deb
```

参考: http://docs.w3af.org/en/latest/advanced-install.html#installing-using-virtualenv  


2017/11/29  
