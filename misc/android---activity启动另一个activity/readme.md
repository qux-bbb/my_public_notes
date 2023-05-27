# android---activity启动另一个activity

```java
Intent intent = new Intent(MainActivity.this,Main2Activity.class);
intent.putExtra("NAME","张三");  // 传递参数，根据需要填写
startActivity(intent);
```


2017/9/2  
