# pacman

pacman - package manager utility, Arch、Manjaro的软件包管理器。  

简单使用  
```bash
# Download and install gpm including dependencies.
pacman -S gpm
# Install ceofhack-0.6-1 package from a local file.
pacman -U /home/user/ceofhack-0.6-1-x86_64.pkg.tar.gz
# Remove a package and all packages that depend on the package, clean cache
pacman -Rsc fcitx 
# Update package list and upgrade all packages afterwards.
pacman -Syu
# Forece Update package list and upgrade all packages afterwards.
pacman -Syyu
# Update package list, upgrade all packages, and then install gpm if it wasn’t already installed.
pacman -Syu gpm
```

选项解释  
```
-S, --sync
    Synchronize packages. Packages are installed directly from the
    remote repositories, including all dependencies required to run
    the packages.
-U, --upgrade
    Upgrade or add package(s) to the system and install the
    required dependencies from sync repositories. Either a URL or
    file path can be specified.
-R, --remove
    Remove package(s) from the system. Groups can also be specified
    to be removed, in which case every package in that group will
    be removed.

REMOVE OPTIONS (APPLY TO -R)
    -s, --recursive
        Remove each target specified including all of their
        dependencies, provided that (A) they are not required by other
        packages; and (B) they were not explicitly installed by the
        user. This operation is recursive and analogous to a backwards
        --sync operation, and it helps keep a clean system without
        orphans. If you want to omit condition (B), pass this option
        twice.
    -c, --cascade
        Remove all target packages, as well as all packages that depend
        on one or more target packages. This operation is recursive and
        must be used with care, since it can remove many potentially
        needed packages.

SYNC OPTIONS (APPLY TO -S)
       -u, --sysupgrade
           Upgrades all packages that are out-of-date.
       -y, --refresh
           Download a fresh copy of the master package database from the 
           server(s) defined in pacman.conf(5). This should typically be 
           used each time you use --sysupgrade or -u. Passing two 
           --refresh or -y flags will force a refresh of all package databases, even if they appear to be up-to-date.
```

参考man手册  


2021/5/4  
