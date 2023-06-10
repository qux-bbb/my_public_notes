# Arduino-Leonardo模拟BadUSB

Arduino Leonardo //小型单片机模拟USB  
貌似Arduino只有这个型号是支持Keyboard操作的  

演示代码如下：  
```c
#include<Keyboard.h>
void setup(){
Keyboard.begin();
delay(1000);
Keyboard.press(KEY_CAPS_LOCK);
delay(500);
Keyboard.press(KEY_LEFT_GUI); //win键
delay(500);
Keyboard.press('r');
delay(500);
Keyboard.release('r');
delay(500);
Keyboard.release(KEY_LEFT_GUI);
delay(500);
Keyboard.println("cmd");
delay(500);
Keyboard.press(KEY_RETURN);
delay(500);
Keyboard.release(KEY_RETURN);
delay(500);
Keyboard.println("i gOT yOU!!!");
delay(500);
Keyboard.release(KEY_CAPS_LOCK);
delay(500);
Keyboard.end();
}

void loop(){}
```

原链接: http://www.freebuf.com/sectool/107242.html#respond  


2016/9/28  
