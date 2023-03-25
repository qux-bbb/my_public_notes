# java---同步

## 单机同步  
使用synchronized lock

例子：  
```java  
// 10个人过山洞
public class Pass implements Runnable{  
    private Object lock=new Object();  
    public void run(){  
        synchronized(lock){  
            System.out.println(Thread.currentThread().getName());  
            try{  
                Thread.sleep(1000);  
            }catch(InterruptedException e){  
                e.printStackTrace();  
            }  
        }  
    }  
      
    public static void main(String[] args){  
        Pass p=new Pass();  
        new Thread(p,"ONE").start();  
        new Thread(p,"TWO").start();  
        new Thread(p,"THREE").start();  
        new Thread(p,"FOUR").start();  
        new Thread(p,"FIVE").start();  
        new Thread(p,"SIX").start();  
        new Thread(p,"SEVEN").start();  
        new Thread(p,"EIGHT").start();
        new Thread(p,"NINE").start();
        new Thread(p,"TEN").start();
        
    }  
}  
```

## 集群同步  
1. 可以使用悲观锁 例如 redis(setnx) 或者表锁
2. 可以使用乐观锁 例如 给加版本号  


2017/9/14  
