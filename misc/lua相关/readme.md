# lua相关

lua，一个脚本语言。  
官网: http://www.lua.org  
文档: http://www.lua.org/pil/contents.html  

linux安装：  
```r
# 安装5.3版本
sudo apt install lua5.3
# luarocks相当于python的pip，装一下：  
sudo apt install luarocks
```

简单用法：  
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

参考链接: https://zhuanlan.zhihu.com/p/582750739  


2020/11/22  
