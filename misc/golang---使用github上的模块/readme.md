# golang---使用github上的模块

### 创建一个新的Go项目

1. 创建一个新的目录来保存你的Go项目：

    ```bash
    mkdir my-github-module-demo
    cd my-github-module-demo
    ```

2. 初始化一个新的Go模块：

    ```bash
    go mod init github.com/yourusername/my-github-module-demo
    ```

   这将在当前目录下创建一个`go.mod`文件。

### 在Go文件中导入GitHub模块

1. 在项目目录里，创建一个新的Go文件，比如`main.go`。

    在这个Go文件中，你可以导入你想使用的GitHub模块。例如，假设你想使用来自GitHub的`gorilla/mux`路由库：

    ```go
    package main

    import (
        "fmt"
        "net/http"
        "github.com/gorilla/mux"
    )

    func YourHandler(w http.ResponseWriter, r *http.Request) {
        w.Write([]byte("Hello, world!"))
    }

    func main() {
        r := mux.NewRouter()
        r.HandleFunc("/", YourHandler)
        http.Handle("/", r)
        fmt.Println("Server is listening...")
        http.ListenAndServe(":8000", nil)
    }
    ```

### 获取和安装模块

1. 执行以下命令来获取和安装该模块：

    ```bash
    go get -u github.com/gorilla/mux
    ```

2. 一旦依赖安装完成，你就可以运行你的Go应用了：

    ```bash
    go run main.go
    ```

    如果一切正常，你将看到输出`Server is listening...`，并且服务器将开始在端口8000上监听。

这样，你就成功地使用了一个来自GitHub的Go模块。这个模块和依赖信息都会记录在`go.mod`文件中，以便未来使用。

### 来源
chatgpt  


---
2023/9/14  
