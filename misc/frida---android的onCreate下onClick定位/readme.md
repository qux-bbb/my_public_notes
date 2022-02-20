# frida---android的onCreate下onClick定位

代码如下：  
```java
public class MainActivity extends AppCompatActivity {
    EditText m;
    Button n;
    String o;
    c p;

    /* access modifiers changed from: protected */
    public void onCreate(Bundle bundle) {
        super.onCreate(bundle);
        setContentView((int) R.layout.activity_main);
        this.n = (Button) findViewById(R.id.button);
        this.m = (EditText) findViewById(R.id.editText);
        this.n.setOnClickListener(new View.OnClickListener() {
            public void onClick(View view) {
                MainActivity mainActivity;
                String str;
                MainActivity.this.o = MainActivity.this.m.getText().toString();
                MainActivity.this.p = new c();
                if (MainActivity.this.o == null) {
                    mainActivity = MainActivity.this;
                    str = "Need Input";
                } else if (MainActivity.this.p.a(MainActivity.this.o)) {
                    mainActivity = MainActivity.this;
                    str = "Congratulations";
                } else {
                    mainActivity = MainActivity.this;
                    str = "Wrong Flag";
                }
                Toast.makeText(mainActivity, str, 1).show();
            }
        });
    }
}
```

可以发现 onClick 其实是一个匿名类的方法，因为是 MainActivity 的第 1 个匿名类，所以定位 onClick 应该是：  
`MainActivity$1.onClick`  

在 frida 的 js 里应该这么写：  
```js
  var mClass = Java.use('ctf.crack.java.MainActivity$1')
  var onClick = mClass.onClick;
```

参考: https://stackoverflow.com/questions/60236107/how-to-hook-into-onclick-method-inside-a-method-using-frida  


---
2021/3/7  
