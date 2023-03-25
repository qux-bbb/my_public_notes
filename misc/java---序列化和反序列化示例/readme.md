# java---序列化和反序列化示例

Person类  
```java
package test;

import java.io.Serializable;

public class Person implements Serializable{
	
	private static final long serialVersionUID = 3390583810947014387L;
	private int age;
	private String name;
	private String sex;
	
	public int getAge() {
		return age;
	}
	public void setAge(int age) {
		this.age = age;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getSex() {
		return sex;
	}
	public void setSex(String sex) {
		this.sex = sex;
	}	
}
```


主类  
```java
package test;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.text.MessageFormat;

import test.Person;

public class TestObjSerializeAndDeserialize {

	private static void SerializePerson() throws FileNotFoundException, IOException {
		Person person = new Person();
		person.setName("Alice");
		person.setAge(23);
		person.setSex("female");
		// ObjectOutputStream 对象输出流，将Person对象存储到D盘的Person.txt文件中，完成对Person对象的序列化操作
		ObjectOutputStream oo = new ObjectOutputStream(new FileOutputStream(new File("D:/Person.txt")));
		oo.writeObject(person);
		System.out.println("Person对象序列化成功！");
		oo.close();
	}

	private static Person DeserializePerson() throws Exception, IOException {
		ObjectInputStream oi = new ObjectInputStream(new FileInputStream(new File("D:/Person.txt")));
		Person person = (Person) oi.readObject();
		System.out.println("Person对象反序列化成功！");
		return person;
	}

	public static void main(String[] args) throws Exception {
		SerializePerson();// 序列化Person对象
		Person p = DeserializePerson();// 反序列Person对象
		System.out.println(MessageFormat.format("name={0},age={1},sex={2}", p.getName(), p.getAge(), p.getSex()));

	}

}
```


2019/1/2  
