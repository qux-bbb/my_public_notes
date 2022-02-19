# rust---读写文件

```rust
use std::fs;

fn main(){
    let filename = "test.txt";

    let content = "Hello World!";
    fs::write(filename, content)
        .expect("Something went wrong writing the file");
    println!("write to {}: {}", filename, content);

    let content_r = fs::read_to_string(filename)
        .expect("Something went wrong reading the file");
    println!("read {}: {}", filename, &content_r);
}
```

参考链接: https://doc.rust-lang.org/book/ch12-02-reading-a-file.html  


2022/2/19  
