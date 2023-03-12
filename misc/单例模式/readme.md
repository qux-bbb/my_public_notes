# 单例模式

keywords: Singleton C#  

## 为什么需要单例模式
日常工作经常需要在应用程序中保持一个唯一的实例，如：IO处理，数据库操作等，由于这些对象都要占用重要的系统资源，所以必须限制这些实例的创建或 始终使用一个公用的实例。  

## 概念
保证一个类仅有一个实例，并提供一个访问它的全局访问点  

## 实现方式
下面会有6个不同的单例模式的实现方式，有以下共同点：
1. 单例被定义为sealed，不允许派生
2. 有一个私有的无参构造函数，可以防止其他类实例化它，而且单例类也不应该被继承
3. 一个静态变量用来保存单实例的引用
4. 一个公有静态方法用来获取单实例的引用，如果实例为null即创建一个

### 版本1：线程不安全
```c#
public sealed class Singleton{
    private Singleton(){}
    private static Singleton instance = null;
    public static Singleton Instance{
        get{
            if(instance == null)
                instance = new Singleton();
            return instance;
        }
    }
}
```
以上实现方式适用于单线程环境，在多线程环境下可能得到Singleton类的多个实例  
假如同时有两个线程去判断`(instance==null)`，并且得到的结果为真，那么两个线程都会创建类Singleton的实例，违背了Singleton模式“唯一实例”的初衷。

### 版本2：线程安全
```c#
public sealed class Singleton{
    private Singleton(){}
    private static readonly object SynObject = new object();
    private static Singleton instance = null;
    public static Singleton Instance{
        get{
            lock(SynObject){
                if(instance == null)
                    instance = new Singleton();
            }
            return instance;
        }
    }
}
```
加了一个同步锁，确保多线程下不会创建多个对象实例。  
增加了额外的开销，可能成为影响系统性能的瓶颈。  

### Double Checked Locking
```c#
public sealed class Singleton{
    private Singleton(){}
    private static readonly object SynObject = new object();
    private static Singleton instance = null;
    public static Singleton Instance{
        get{
            if(instance == null){
                lock(SynObject){
                if(instance == null)
                    instance = new Singleton();
                }
            }
            return instance;
        }
    }
}
```
因为加锁是很耗时的操作，先判断该实例是否为null，就可以降低加锁的次数了，速度更快  
缺点比较繁琐

### 利用静态构造函数
```c#
public sealed class Singleton{
    private Singleton(){}
    private static Singleton instance = new Singleton();
    public static Singleton Instance{
        get{
            return instance;
        }
    }
}
```
.NET运行时能够确保只调用一次静态构造函数，这样就能保证只初始化一次instance  
但C#调用静态构造函数是当.NET运行时发现第一次使用一个类型时自动调用，这样有可能会过早创建实例，降低内存的使用效率  

### 按需创建实例
```c#
public sealed class Singleton{
    Singleton(){}
    public static Singleton Instance{
        get{
            return Nested.instance; // Nested 嵌套的
        }
    }

    class Nested{
        static Nested(){}
        internal static readonly Singleton instance = new Singleton();
    }   // internal 内部的
}
```
如果不调用属性Singleton.Instance，就不会触发.NET运行时调用Nested，也不会创建实例，做到了按需创建  


2017/9/22  
