# gopher-lua

https://github.com/yuin/gopher-lua  
GopherLua: VM and compiler for Lua in Go  
使用Go构建的lua的虚拟机和编译器，大概就是可以用go包裹lua脚本运行  

使用示例1  
```go
import (
    "github.com/yuin/gopher-lua"
)

L := lua.NewState()
defer L.Close()
if err := L.DoString(`print("hello")`); err != nil {
    panic(err)
}
```

使用示例2  
```go
import (
    "github.com/yuin/gopher-lua"
)

L := lua.NewState()
defer L.Close()
if err := L.DoFile("hello.lua"); err != nil {
    panic(err)
}
```


2020/11/24  
