# Java中获取键盘输入值的三种方法

## 方法一：从控制台接收一个字符，然后将其打印出来
```java
public static void main(String [] args) throws IOException{
    System.out.print("Enter a Char:");
    char i = (char) System.in.read();
    System.out.println("your char is :"+i);
}
```
虽然此方式实现了从键盘获取输入的字符，但是System.out.read()只能针对一个字符的获取，同时，获取进来的变量的类型只能是char,当我们输入一个数字，希望得到的也是一个整型变量的时候，我们还得修改其中的变量类型，这样就显得比较麻烦。

## 方法二：从控制台接收一个字符串，然后将其打印出来
需要用到BufferedReader类和InputStreamReader类  
```java
public static void main(String [] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String str = null;
    System.out.println("Enter your value:");
    str = br.readLine();
    System.out.println("your value is :"+str);
}
```
这样我们就能获取我们输入的字符串。  

## 方法三：最简单、最强大的，就是用Scanner类
```java
public static void main(String [] args) {
    Scanner sc = new Scanner(System.in);
    System.out.println("请输入你的姓名：");
    String name = sc.nextLine();
    System.out.println("请输入你的年龄：");
    int age = sc.nextInt();
    System.out.println("请输入你的工资：");
    float salary = sc.nextFloat();
    System.out.println("你的信息如下：");
    System.out.println("姓名："+name+"\n"+"年龄："+age+"\n"+"工资："+salary);
}
```


原链接: http://soft.chinabyte.com/database/191/12466191.shtml  


---
2016/6/5  
