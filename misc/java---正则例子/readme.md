# java---正则例子

查找是否包含子字符串：  
```java
package test;

import java.util.regex.Pattern;

public class Hello {

	public static void main(String[] args) {
		String content = "I am noob" + "from runoob.com.";
		String pattern = ".*runoob.*";

		boolean isMatch = Pattern.matches(pattern, content);
		System.out.println(isMatch);
	}
}
```

查找并输出结果：  
```java
package test;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Hello {

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
}

/*
Found value:This order was placed for QT3000! OK?
Found value:This order was placed for QT
Found value:3000
Found value:! OK?
*/
```

原链接: https://www.runoob.com/java/java-regular-expressions.html  


2017/3/20  
