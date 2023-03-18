# java---遍历Map获取键值对

第一种方法是根据map的 `keyset()` 方法来获取key的set集合，然后遍历map取得value的值：  
```java
package HashMapTest2;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Set;

public class HashMapTest2 {
	@SuppressWarnings({ "rawtypes", "unchecked" })
	public static void main(String[] args) {
		HashMap map = new HashMap();

		map.put("a", "aaaa");
		map.put("b", "bbbb");
		map.put("c", "cccc");
		map.put("d", "dddd");

		Set set = map.keySet();

		for (Iterator iter = set.iterator(); iter.hasNext();) {
			String key = (String) iter.next();
			String value = (String) map.get(key);
			System.out.println(key + "====" + value);
		}
	}
}
```

第二种方式是使用 `Map.Entry` 来获取：  
```java
package HashMapTest4;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;

public class HashMapTest4 {
	@SuppressWarnings({ "rawtypes", "unchecked" })
	public static void main(String[] args) {
		HashMap map = new HashMap();

		map.put("a", "aa");
		map.put("b", "bb");
		map.put("c", "cc");
		map.put("d", "dd");

		Set set = map.entrySet();

		for (Iterator iter = set.iterator(); iter.hasNext();) {
			Map.Entry entry = (Map.Entry) iter.next();

			String key = (String) entry.getKey();
			String value = (String) entry.getValue();
			System.out.println(key + ": " + value);
		}
	}
}
```


原链接: http://blog.sina.com.cn/s/blog_7750745b0101c09d.html  


2016/5/13  
