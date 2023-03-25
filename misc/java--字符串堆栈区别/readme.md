# java--字符串堆栈区别

``` java
// 例一：
String str1 = "abc";
String str2 = "abc";
System.out.println(str1==str2); //true

// 例二：
String str1 =new String ("abc");
String str2 =new String ("abc");
System.out.println(str1==str2); // false
```

为什么一个true，一个false？  
**直接声明变量**，变量会在栈中被创建，如果栈中已经有这样的变量值，新声明的变量会指向这样的变量值，也就是**内存共享**  
**new生成对象**的话，会在堆中被创建，就算值一样，也会创建两个实例  


2017/9/16  
