# frida---android获取类成员值

```python
import frida, sys

def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)

jscode = """
Java.perform(function () {
  var MainActivity = Java.use('ctf.crack.java.MainActivity');
  var c = Java.use('ctf.crack.java.c');

  // Anonymous class
  var mClass = Java.use('ctf.crack.java.MainActivity$1');
  var onClick = mClass.onClick;
  onClick.implementation = function (v) {
    // we have methods with the same name as class field, then we need _ before variable name to get the variable
    console.log(JSON.stringify(c._a.value));

    // Call the original onClick handler
    onClick.call(this, v);

    console.log('done');
  };
});
"""

process = frida.get_usb_device().attach('ctf.crack.java')
script = process.create_script(jscode)
script.on('message', on_message)
print('[*] Running')
script.load()
sys.stdin.read()
```

参考链接: https://stackoverflow.com/questions/58970738/frida-print-static-variable-of-a-class  


---
2020/6/4  
