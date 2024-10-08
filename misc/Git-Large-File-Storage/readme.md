# Git Large File Storage

keywords: git 大文件  

官网: https://git-lfs.com/  
github地址: https://github.com/git-lfs/git-lfs  

Git LFS is a command line extension and specification for managing large files with Git.  

The client is written in Go, with pre-compiled binaries available for Mac, Windows, Linux, and FreeBSD. Check out the website for an overview of features.  

安装：  
```r
git lfs install
```

针对psd文件进行配置：  
```r
git lfs track "*.psd"
git add .gitattributes
```

然后就可以正常使用了  
```r
git add file.psd
git commit -m "Add design file"
git push
```


2024/10/8  
