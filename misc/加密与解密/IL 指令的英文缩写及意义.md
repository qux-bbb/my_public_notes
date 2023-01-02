IL 指令的英文缩写及意义  

操作数  
```
缩写        展开        意义
i1          int8        1 字节有符号整型数
i4          int32       4 字节有符号整型数
i8          int64       8 字节有符号整型数
u1          uint8       1 字节无符号整型数
u4          uint32      4 字节无符号整型数
f4          float32     4 字节浮点数
f8          float64     8 字节浮点数
```

操作符  
```
缩写        展开              意义
ld          load              读入
st          set               赋值
loc         local             本地变量
arg         argument          方法的参数
s           short             短指令
c           const             常量
inst        instance          （对象的）实例
gt          great than        大于
lt          less than         小于
eq          equal             等于
ne          not equal         不等于
br 和 b     branch            跳转
ind         indirect          非直接（间接，即取变量地址）
conv        convert           转换
virt        virtual           虚的（虚函数）
fld         field             操作对象是 field
a           address           （变量的）地址
elem        element           元素（指 array 类型）
ovf         over flow         带溢出的
ftn         function pointer  方法（函数的指针）
```