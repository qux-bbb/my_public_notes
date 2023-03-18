# golang简单了解

keywords: go相关 golang相关  

官网: https://go.dev/  
官方文档: https://go.dev/doc/  

据说好写并且速度快。  
查看版本: `go version`  


## hello world 例子  
test.go  
```go
// https://stackoverflow.com/questions/14094190/function-similar-to-getchar/17278730#17278730
package main

import (
    "fmt"
    "os"
)

func main() {
    fmt.Println("Hello, World!")
    content := make([]byte, 1)
    os.Stdin.Read(content)
}
```

运行  
```r
go run test.go
```

构建可执行文件  
```r
go build test.go

# 在linux下构建windows下32位程序(windows不支持这样构建) 参考: https://www.cnblogs.com/52why/p/15479283.html
GOOS=windows GOARCH=386 go build hello.go
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


## 下载添加包和依赖
下载添加或升级到最新版：  
```r
go get example.com/pkg
```

下载添加或修改为指定版本(升级或降级)：  
```r
go get example.com/pkg@v1.2.3
```

移除包或依赖：  
```r
go get example.com/pkg@none
```


## 编译添加程序和依赖
编译安装最新版本：  
```r
go install golang.org/x/tools/gopls@latest
```

根据当前目录下的 `go.mod` 编译安装相应版本：  
```r
go install golang.org/x/tools/gopls
```


---
2020/11/23  
