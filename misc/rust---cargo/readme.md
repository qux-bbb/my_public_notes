# rust---cargo

cargo是rust的构建工具和包管理器。  

构建过程演示：  
```r
# 生成一个初始项目，默认会生成src/main.rs, 写了helloworld
cargo new hello
# 进入相关文件夹
cd hello
# 构建调试用的二进制文件，在target/debug文件夹下
cargo build
# 构建发布用的二进制文件，在target/release文件夹下
cargo build --release 
```

包管理器功能，使用cargo下载构建tealdeer：  
```r
cargo install tealdeer
```


2022/2/19  
