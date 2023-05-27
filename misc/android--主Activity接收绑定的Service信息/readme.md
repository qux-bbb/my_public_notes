# android--主Activity接收绑定的Service信息

Service代码：  
```java
public class MyService extends Service {

    int time = 5;

    private MyBinder myBinder = new MyBinder();

    @Override
    public IBinder onBind(Intent intent) {
        return myBinder;
    }

    class MyBinder extends Binder{
        int getTime(){
            return time;
        }
    }
}
```

Main Activity代码：  
```java
public class MainActivity extends Activity {

    String TAG = "MainActivity";

    MyService.MyBinder myBinder;

    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        Log.v(TAG, "onCreate");
        setContentView(R.layout.activity_main);

        final TextView textView = (TextView)findViewById(R.id.textView);
        Button button = (Button) findViewById(R.id.button);


        final ServiceConnection connection = new ServiceConnection() {
            @Override
            public void onServiceConnected(ComponentName name, IBinder service) {

                myBinder = (MyService.MyBinder) service;
                int time = myBinder.getTime();
                textView.setText("The time is: " + time);
            }

            @Override
            public void onServiceDisconnected(ComponentName name) {
            }
        };

        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                final Intent intent  = new Intent(MainActivity.this,MyService.class);
                bindService(intent,connection,BIND_AUTO_CREATE);
            }
        });
    }

}
```


2017/9/2  
