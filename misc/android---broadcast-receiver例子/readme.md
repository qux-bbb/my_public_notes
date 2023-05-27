# android---broadcast-receiver例子

直接写在Activity里的broadcast receiver，也有把intent filter写在AndroidManifest.xml里的，都可以  
```java
public class MainActivity extends Activity {

    String TAG = "MainActivity";

    TextView textView;
    MyReceiver myReceiver;

    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        Log.v(TAG, "onCreate");
        setContentView(R.layout.activity_main);

        textView = (TextView)findViewById(R.id.textView);
        Button button = (Button) findViewById(R.id.button);


        // 创建意图过滤器，只接收这样的广播
        IntentFilter intentFilter = new IntentFilter();
        intentFilter.addAction("hello");

        myReceiver = new MyReceiver();
        registerReceiver(myReceiver,intentFilter);


        // 点击按钮发送广播
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // hello 的广播
                Intent intent = new Intent("hello");
                sendBroadcast(intent);
                // World 的广播
                Intent intent1 = new Intent("World!");
                sendBroadcast(intent1);
            }
        });
    }


    class MyReceiver extends BroadcastReceiver{

        @Override
        public void onReceive(Context context, Intent intent) {
            Toast.makeText(MainActivity.this, "接到广播：" + intent.getAction(), Toast.LENGTH_SHORT).show();
        }
    }


    @Override
    protected void onDestroy() {
        super.onDestroy();
        // 结束，取消广播接收
        unregisterReceiver(myReceiver);
    }
}
```


2017/9/2  
