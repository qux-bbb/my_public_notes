# android---AsyncTask例子

```java
// 打开蓝牙的AsyncTask
private class OpenBlueTask extends AsyncTask<String, String, String> {

    // 等待提示框
    ProgressDialog waitDialog = new ProgressDialog(MainActivity.this);


    @Override
    protected void onPreExecute() {
        super.onPreExecute();
        waitDialog.setMessage(getString(R.string.opening_blue));
        waitDialog.setCancelable(false);
        waitDialog.show();

    }

    @Override
    protected String doInBackground(String... params) {
        bluetoothAdapter.enable();
        // 休眠3秒，等待蓝牙开启
        try {
            Thread.sleep(3000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        return null;
    }

    @Override
    protected void onPostExecute(String s) {
        super.onPostExecute(s);
        waitDialog.dismiss();
        if(bluetoothAdapter.isEnabled()){
            Toast.makeText(MainActivity.this, R.string.open_blue_success, Toast.LENGTH_SHORT).show();
            // 显示已配对设备
            showPairedDevices();
        }else{
            Toast.makeText(MainActivity.this, R.string.open_blue_failure, Toast.LENGTH_SHORT).show();
        }
    }
}
```


2017/9/2  
