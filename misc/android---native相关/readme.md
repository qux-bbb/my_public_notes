android一般是用java或者kotlin写的，这两种语言生成的逻辑用虚拟机执行，效率较低，而且很容易被反编译到源码级别，这个时候就出现了native层。  
native层用C或C++编写。  

用Android Studio创建一个新项目，选择`Native C++`，大概看一下。  


MainActivity.kt  
```c++
package com.example.nativetest

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.TextView

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // Example of a call to a native method
        findViewById<TextView>(R.id.sample_text).text = stringFromJNI() + "\n" + "1+2=" + add(1, 2);
    }

    /**
     * A native method that is implemented by the 'native-lib' native library,
     * which is packaged with this application.
     */
    external fun stringFromJNI(): String
    external fun add(a: Int, b: Int): Int

    companion object {
        // Used to load the 'native-lib' library on application startup.
        init {
            System.loadLibrary("native-lib")
        }
    }
}
```

nativa-lib.cpp  
```c++
#include <jni.h>
#include <string>

extern "C" JNIEXPORT jstring JNICALL
Java_com_example_nativetest_MainActivity_stringFromJNI(
        JNIEnv* env,
        jobject /* this */) {
    std::string hello = "Hello from C++";
    return env->NewStringUTF(hello.c_str());
}

extern "C" JNIEXPORT jint JNICALL
Java_com_example_nativetest_MainActivity_add(
        JNIEnv* env,
        jobject /* this */,
        jint a,
        jint b) {
    return a+b;
}
```

可以发现调用的时候，前2个参数是固定的，逆向的时候可以用到  
IDA里，打开.so文件，找到一个方法，选择第1个参数，右键 `Set lvar type`, 设置为 `JNIEnv*`, 就能看到很多api的名字了，方便理解逻辑  
这叫 还原JNI函数方法名  


参考：  
https://blog.mindorks.com/getting-started-with-android-ndk-android-tutorial  
https://www.cnblogs.com/chenxibobo/p/6491976.html  
