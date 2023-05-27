# android---AsyncTask三个泛型参数含义

```
class AsyncTask<Params, Progress, Result>

 AsyncTask的三个泛型参数说明（三个参数可以是任何类型） 
    第一个参数：传入doInBackground()方法的参数类型 
    第二个参数：传入onProgressUpdate()方法的参数类型 
    第三个参数：传入onPostExecute()方法的参数类型，也是doInBackground()方法返回的类型。

举个例子
private class task extends AsyncTask<String, String, String>

//AsyncTask<>的参数类型由用户设定，这里设为三个String
//第一个String代表输入到任务的参数类型，也即是doInBackground()的参数类型
//第二个String代表处理过程中的参数类型，也就是doInBackground()执行过程中的产出参数类型，通过publishProgress()发消息
//传递给onProgressUpdate()一般用来更新界面
//第三个String代表任务结束的产出类型，也就是doInBackground()的返回值类型，和onPostExecute()的参数类型
```


2017/9/2  
