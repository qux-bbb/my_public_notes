# rust了解

据说和C++一样快，但更安全  

官网：https://www.rust-lang.org  
官方文档: https://doc.rust-lang.org/book  
中文社区对官方文档的翻译: https://kaisery.github.io/trpl-zh-cn  

安装方式去官网找一些，针对不同平台介绍的比较清楚  
不要用这种 `sudo apt install cargo` 的方式，会有问题  
安装后可使用 `rustc --version` 确认是否安装成功  
安装后可以在本地查看入门文档: `rustup doc --book`  

编译器：rustc  
自动格式化工具：rustfmt  
构建工具和包管理器：cargo  


## hello world例子  
hello.rs  
```rust
fn main() {
    println!("Hello, world!");
}
```

编译: `rustc hello.rs`, 执行即可生成可执行文件  


20201123
