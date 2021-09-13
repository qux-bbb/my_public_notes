# IDA---创建结构体文件并导入

## 结构体文件
结构体文件可以写成这样:  
```c
// struct.h 
struct student
{
    int id;
    char name[20];
    int age;
};
```

## IDA导入  
File --> Load file --> Parse C header file  

使用时需要先添加到structures中  
View --> Open subviews --> Structures  
按'Insert'键，点击'Add standard structure'添加即可  

注意点: Structure name 需要写真实存在的结构体名称  

这样其实也没有多简单，如果数量少的话，还不如直接用IDA构建结构体  


2019/9/15  
