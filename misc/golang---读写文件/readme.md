# golang---读写文件

ioutil简单读写文件  
```go
package main

import (
    "fmt"
    "io/ioutil"
)

func main() {
    message := []byte("Hello, Gophers!")
    ioutil.WriteFile("hello.txt", message, 0644)

    content, _ := ioutil.ReadFile("hello.txt")
    fmt.Printf("File contents: %s", content)
}
```

os.OpenFile读写文件  
```go
package main

import (
    "fmt"
    "os"
)

func main() {
    message := []byte("Hello, Gophers!")
    fw, _ := os.OpenFile("hello.txt", os.O_WRONLY|os.O_CREATE, 0755)
    fw.Write(message)
    fw.Close()

    fr, _ := os.OpenFile("hello.txt", os.O_RDONLY, 0755)
    stat, _ := fr.Stat()
    content := make([]byte, stat.Size())
    content_size, _ := fr.Read(content)
    fr.Close()
    fmt.Printf("%d: %s\n", content_size, content)
}
```

参考链接：  
1. https://pkg.go.dev/io/ioutil
2. https://pkg.go.dev/os#OpenFile


2022/6/23  
