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
# 运行构建好的二进制文件，如果没有构建，会先构建
cargo run
# 运行构建好的发布用的二进制文件
cargo run --release
# 构建文档，可以很方便查看各个函数的功能和参数
cargo doc
cargo doc --release
# 删除target文件夹
cargo clean
```

包管理器功能，使用cargo下载构建tealdeer：  
```r
cargo install tealdeer
```


2022/2/19  
