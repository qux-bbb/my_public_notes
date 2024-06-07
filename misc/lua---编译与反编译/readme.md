# lua---编译与反编译

## 脚本举例(test.lua)
```lua
-- 单行注释
--[[
    多行注释
]]--

-- 变量声明
hello = 'hello'  -- 也可以是双引号 "hello"
print(hello)
len = string.len(hello)
print(len)
bar = 1 + 2
print(bar)

-- 没有数组，只有table
mytable = {}
mytable.foo = "hello world"
mytable.bar = 1 + 2
print(mytable)

-- 函数示例
function sayhello(name)
    print("hello, "..name)
end
```


## 编译
```bash
luac -o test_compiled test.lua
```

执行编译后的文件：  
```bash
lua ./test_compiled
```


## 反编译
Unluac: https://sourceforge.net/projects/unluac/  

运行前需要安装java环境：  
```bash
sudo apt install openjdk-19-jre
```

运行示例：  
```bash
java -jar unluac.jar test_compiled > test_decompiled.lua
```

反编译的结果不完全等同于原脚本，没有注释  


---
2024/6/7  
