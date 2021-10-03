# pacman---制作软件包

主要文件是 `PKGBUILD`，负责制作的整个过程  
`hello-world.sh` 是功能文件，功能是输出 `Hello to you!`  

`hello-world.sh`  
```r
echo "Hello to you!"
```

`PKGBUILD`  
```r
pkgname=hello-world
pkgver=1.0.0
pkgrel=1
pkgdesc="Hello world in your terminal!"
arch=("x86_64")
licence=("GPL")

source=("hello-world.sh")

sha256sums=("378f8931ff9a2e10b7ca2ebf1ab4067d588789f7e1ac007f5f20af2288814526")

package() {
  mkdir -p "${pkgdir}/usr/bin"
  cp "${srcdir}/hello-world.sh" "${pkgdir}/usr/bin/hello-world"
  chmod +x "${pkgdir}/usr/bin/hello-world"
}
```

将 `hello-world.sh` 和 `PKGBUILD` 放在同一目录下，执行 `makepkg`，会生成 src 和 pkg 文件夹，hello-world-1.0.0-1-x86_64.pkg.tar.zst 文件  
zst文件即为软件包，可使用pacman安装：  
```r
pacman -U hello-world-1.0.0-1-x86_64.pkg.tar.zst
```

安装之后执行 `hello-world` 命令，即可输出字符串  

测试之后可以卸载：  
```r
pacman -Rsc hello-world
```


参考链接：  
1. https://linux.cn/article-13843-1.html
2. https://wiki.archlinux.org/title/PKGBUILD


2021/10/3  
