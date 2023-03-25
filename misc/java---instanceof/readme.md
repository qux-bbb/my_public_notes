# java---instanceof

instanceof 运算符可以用来在运行时判断对象是否为特定类的一个实例  

例子：
```java
public class Main {
	public static void main(String[] args) {
		Integer i = new Integer(9);
		boolean b = i instanceof Object;
		System.out.println(b);
	}
}
```
输出：true  


2017/9/21  
