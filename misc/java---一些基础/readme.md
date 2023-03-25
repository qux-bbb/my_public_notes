# java---一些基础

## 输出
```java
System.out.println("hello");
```

## number和math常用方法
```java
equals() 判断number对象是否与参数相等。
toString() 以字符串形式返回值。
parseInt() 将字符串解析为int类型。
abs() 返回参数的绝对值。
ceil() 对变量向上取整，返回类型为double型。
floor() 对变量向下取整。返回类型为double类型。
round() 返回一个最接近的int、long型值。
min() 返回两个参数中的最小值。
max() 返回两个参数中的最大值。
pow() 返回第一个参数的第二个参数次方。
sqrt() 求参数的算术平方根。
random() 返回一个随机数。
```

## charactor常用方法
```java
isLetter() 是否是一个字母
isDigit() 是否是一个数字字符
isWhitespace() 是否是一个空格
isUpperCase() 是否是大写字母
isLowerCase() 是否是小写字母
toUpperCase() 指定字母的大写形式
toLowerCase() 指定字母的小写形式
toString() 返回字符的字符串形式，字符串的长度仅为1
```

## String常用方法
```java
char charAt(int index)
返回指定索引处的 char 值。
  
String concat(String str)
将指定字符串连接到此字符串的结尾。
  
boolean endsWith(String suffix)
测试此字符串是否以指定的后缀结束。
  
int length()
返回此字符串的长度。
  
String replace(char oldChar, char newChar)
返回一个新的字符串，它是通过用 newChar 替换此字符串中出现的所有 oldChar 得到的。
  
String[] split(String regex)
根据给定正则表达式的匹配拆分此字符串。
  
char[] toCharArray()
将此字符串转换为一个新的字符数组。
  
String toLowerCase()
使用默认语言环境的规则将此 String 中的所有字符都转换为小写。
  
String toUpperCase(Locale locale)
使用给定 Locale 的规则将此 String 中的所有字符都转换为大写。
  
String trim()
返回字符串的副本，忽略前导空白和尾部空白。
```

## 数组
定义数组  
```java
double[] myList = new double[size];
```

foreach结构输出数组元素  
```java
for (double element: myList) {
    System.out.println(element);
 }
 ```
  
二维数组  
```java
int a[][] = new int[2][3];
```

java 自带数组排序  
```java
int a[] = {2,3,4,5,1};
Arrays.sort(a);
```
Arraylist java动态数组  
```java
ArrayList<Integer> aa = new ArrayList<Integer>();  
```

## 读取输入
使用 BufferedReader 在控制台读取字符
```java 
import java.io.*;

public class BRRead {
	public static void main(String args[]) throws IOException {
		char c;
		// 使用 System.in 创建 BufferedReader
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		System.out.println("输入字符, 按下 'q' 键退出。");
		// 读取字符
		do {
			c = (char) br.read();
			System.out.println(c);
		} while (c != 'q');
	}
}
```
  
Scanner 读取  
```java  
import java.util.Scanner;

public class ScannerDemo {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		// 从键盘接收数据

		// next方式接收字符串
		System.out.println("next方式接收：");
		// 判断是否还有输入
		if (scan.hasNext()) {
			String str1 = scan.next();
			System.out.println("输入的数据为：" + str1);
		}

	}
}
```
   
## 正则
是否包含  
```java
	public static void main(String[] args) {
		String content = "I am noob" + "from runoob.com.";
		String pattern = ".*runoob.*";

		boolean isMatch = Pattern.matches(pattern, content);
		System.out.println(isMatch);
	}
```

查找并输出  
```java
	public static void main(String[] args) {
		String line = "This order was placed for QT3000! OK?";
		String pattern = "(\\D*)(\\d+)(.*)";

		Pattern r = Pattern.compile(pattern);

		Matcher m = r.matcher(line);
		if (m.find()) {
			for (int i = 0; i < m.groupCount() + 1; i++) {
				System.out.println("Found value:" + m.group(i));
			}
		} else {
			System.out.println("No match");
		}
	}
```

## 设置输出小数位数  
```java
BigDecimal bd = new BigDecimal(3.112);   
bd = bd.setScale(2,BigDecimal.ROUND_HALF_UP);    
System.out.println(bd);
```

## 栈操作

```java
Stack<Integer> sk = new Stack<Integer>();
sk.push(1);  // 压栈
sk.pop();	 // 弹栈
sk.peek();   // 看栈最上的元素	
```

## 队列操作
```java
Queue<Integer> que = new LinkedList<Integer>();
que.offer(1);
que.poll();
que.peek();
```

## 重载和重写
重载（Overloading）  
方法名相同，参数的个数/类型不同，返回值可同可不同  
重写（Overrding）  
子类中的一个方法跟父类比较，方法名，参数表，返回类型完全相同，也称为方法覆盖  

## java的异常
```r
Throwable
    1.Error
    2.Exception
        2.1 IOException
        2.2 RuntimeException
```

## 2种List
ArrayList   基于数组，随机访问更快  
LinkedList  基于链表，添加、删除更快  


参考链接: https://www.runoob.com/java/java-number.html  


2017/3/19  
