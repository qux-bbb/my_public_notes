# rpm-yum-dnf

rpm、yum、dnf都是包管理器，关系类似dpkg、apt-get、apt的关系。  


## rpm
rpm, Redhat Package Manager, 只能安装单个包，不能解决依赖问题。  

```r
QUERYING AND VERIFYING PACKAGES:
    rpm {-q|--query} [select-options] [query-options]
    rpm --querytags
    rpm {-V|--verify} [select-options] [verify-options]
INSTALLING, UPGRADING, AND REMOVING PACKAGES:
    rpm {-i|--install} [install-options] PACKAGE_FILE ...
    rpm {-U|--upgrade} [install-options] PACKAGE_FILE ...
    rpm {-F|--freshen} [install-options] PACKAGE_FILE ...
    rpm {--reinstall} [install-options] PACKAGE_FILE ...
    rpm {-e|--erase} [--allmatches] [--justdb] [--nodeps] [--noscripts]
        [--notriggers] [--test] PACKAGE_FILE ...
```

举例：  
```r
# Show version of httpd package
rpm --query httpd
# Show changed, missing and/or incorrectly installed files of matching packages
rpm --verify --all 'php-*'
```


## yum
yum, Yellow dog Updater, Modified 可以自动下载安装依赖，解决大部分依赖问题  
```r
# Find the package that provides a particular command:
yum provides command
# Install a new package:
yum install package
# Install a new package and assume yes to all questions (also works with update, great for automated updates):
yum -y install package
# Remove a package:
yum remove package
# Display available updates for installed packages:
yum check-update
# Upgrade installed packages to the newest available versions:
yum upgrade
```


## dnf
dnf, Dandified Yum, Dandified是打扮漂亮的意思，用于取代yum  
```r
# Search packages via keywords:
dnf search keywords
# Find which packages provide a given file:
dnf provides file
# Install a new package:
sudo dnf install package
# Install a new package and assume yes to all questions:
sudo dnf -y install package
# List installed packages:
dnf list --installed
# Display details about a package:
dnf info package
# Remove a package:
sudo dnf remove package
# Upgrade installed packages to the newest available versions:
sudo dnf upgrade
```


## 参考链接
https://blog.csdn.net/qq_47346664/article/details/120277985  
https://www.linuxprobe.com/aptyum-dnfpkg-diff.html  
tldr  


---
2022/7/1  
