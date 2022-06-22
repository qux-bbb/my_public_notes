# golang---http

使用http模块可以发起http或https请求。  

简单的get请求示例  
```go
package main

import (
	"fmt"
	"io"
	"log"
	"net/http"
)

func main() {
	res, err := http.Post("http://example.com")
	if err != nil {
		log.Fatal(err)
	}
	body, err := io.ReadAll(res.Body)
	res.Body.Close() // 一定要关掉以免造成内存泄漏
	if res.StatusCode > 299 {
		log.Fatalf("Response failed with status code: %d and\nbody: %s\n", res.StatusCode, body)
	}
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("%s", body)
}
```

原链接: https://pkg.go.dev/net/http?GOOS=windows#pkg-examples  


2022/6/22  
