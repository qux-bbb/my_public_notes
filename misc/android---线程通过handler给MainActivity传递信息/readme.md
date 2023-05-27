# android---线程通过handler给MainActivity传递信息

```java
final TextView textView = (TextView)findViewById(R.id.textView);
Button button = (Button) findViewById(R.id.button);

final Handler handler;

handler = new Handler(){
    @Override
    public void handleMessage(Message msg) {
        super.handleMessage(msg);
        textView.setText(msg.obj.toString());
    }
};


button.setOnClickListener(new View.OnClickListener() {
    @Override
    public void onClick(View v) {
        new Thread(new Runnable() {
            @Override
            public void run() {
                int time = 5;
                while(true){
                    try {
                        Thread.sleep(1000);
                        Message message = new Message();
                        if (time > 0){
                            message.obj = "Wait for " + time + " s.";
                            time -= 1;
                        }else{
                            message.obj = "I love you!";
                            handler.sendMessage(message);
                            return;
                        }

                        handler.sendMessage(message);

                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
            }
        }).start();
    }
});
```


2017/9/2  
