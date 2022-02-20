# frida---android

## 安装与测试
官方入门文档 https://www.frida.re/docs/android/  

安装frida  
```r
$ pip install frida-tools
```

在这里下载合适的frida-server: [releases page](https://github.com/frida/frida/releases)  
就是 frida-server 开头的，不要下错了  

在设备运行frida-server  
```r
$ adb root # might be required
$ adb push frida-server /data/local/tmp/ 
$ adb shell "chmod 755 /data/local/tmp/frida-server"
$ adb shell "/data/local/tmp/frida-server &"
```

确保可以看到设备  
```r
$ adb devices -l
```

列出当前进程  
```r
$ frida-ps -U
```

监控某个应用  
```r
frida-trace -U -i open com.google.android.calendar
```

打开日历就能看到一些操作记录  


## 实例
https://www.frida.re/docs/examples/android/  
上面已经启动了frida-server，接着下载[apk](https://github.com/ctfs/write-ups-2015/tree/master/seccon-quals-ctf-2015/binary/reverse-engineering-android-apk-1)，安装到模拟器里  
```r
adb install rps.apk
```
把app打开  
把下面的代码保存成ctf.py，`python ctf.py`，然后在app里随便点一个就能拿到flag  
```python
import frida, sys

def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)

jscode = """
Java.perform(function () {
  // Function to hook is defined here
  var MainActivity = Java.use('com.example.seccon2015.rock_paper_scissors.MainActivity');

  // Whenever button is clicked
  var onClick = MainActivity.onClick;
  onClick.implementation = function (v) {
    // Show a message to know that the function got called
    send('onClick');

    // Call the original onClick handler
    onClick.call(this, v);

    // Set our values after running the original onClick handler
    this.m.value = 0;
    this.n.value = 1;
    this.cnt.value = 999;

    // Log to the console that it's done, and we should have the flag!
    console.log('Done:' + JSON.stringify(this.cnt));
  };
});
"""

process = frida.get_usb_device().attach('com.example.seccon2015.rock_paper_scissors')
script = process.create_script(jscode)
script.on('message', on_message)
print('[*] Running CTF')
script.load()
sys.stdin.read()
```

这个app比较简单，主要逻辑:  
```java
if (1000 == MainActivity.this.cnt) {
    tv3.setText("SECCON{" + String.valueOf((MainActivity.this.cnt + MainActivity.this.calc()) * 107) + "}");
}
```
`MainActivity.this.calc()`在lib*.so里，这里直接返回了7，但真实情况应该是比较复杂的受保护的逻辑，使用frida就可以直接绕过保护，得到结果  


---
2020/5/21  
