# golang简单了解

官网：https://go.dev/  
据说好写并且速度快。  
查看版本: `go version`  


## hello world 例子  
test.go  
```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```

运行  
```
go run test.go
```

构建可执行文件  
```
go build test.go
```


## web例子
```go
package main

import (
    "fmt"
    "net/http"
)

func main() {
    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        fmt.Fprintf(w, "Hello, you've requested: %s\n", r.URL.Path)
    })

    http.ListenAndServe(":80", nil)
}
```
原链接: https://gowebexamples.com/hello-world/  


## 安装模块示例  
```
go get github.com/yuin/gopher-lua
```


2020/11/23  
