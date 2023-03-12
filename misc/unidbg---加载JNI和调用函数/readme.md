# unidbg---加载JNI和调用函数

通过吾爱破解的2023春节解题领红包的Android高级题学一下unidbg具体怎么用  
活动地址: https://www.52pojie.cn/thread-1738015-1-1.html  
Android高级题WP: https://www.52pojie.cn/forum.php?mod=viewthread&tid=1742121&extra=page%3D1%26filter%3Dtypeid%26typeid%3D344&page=1#45541643_android-%E9%AB%98%E7%BA%A7%E9%A2%98-1/28  

配置好unidbg之后，从apk文件里取出lib52pojie.so  
在 unidbg-android/src/test/java/com/zj/ 下放2个文件: lib52pojie.so, wuaipojie2023_2.java  
wuaipojie2023_2.java 内容如下：  
```java
package com.zj;

import com.github.unidbg.AndroidEmulator;
import com.github.unidbg.linux.android.AndroidEmulatorBuilder;
import com.github.unidbg.linux.android.AndroidResolver;
import com.github.unidbg.linux.android.dvm.DalvikModule;
import com.github.unidbg.linux.android.dvm.VM;
import com.github.unidbg.memory.Memory;
import com.github.unidbg.virtualmodule.android.AndroidModule;

import java.io.File;

public class wuaipojie2023_2 {

    public static void main(String[] args) {
        AndroidEmulator emulator = AndroidEmulatorBuilder.for64Bit().setRootDir(new File("target/rootfs")).setProcessName("com.zj.wuaipojie2023_2").build();
        Memory memory = emulator.getMemory();
        memory.setLibraryResolver(new AndroidResolver(23));

        VM vm = emulator.createDalvikVM();
        vm.setVerbose(true);

        new AndroidModule(emulator, vm).register(memory);

        DalvikModule dm = vm.loadLibrary(new File("unidbg-android/src/test/java/com/zj/lib52pojie.so"), false);

        dm.callJNI_OnLoad(emulator);
    }
}
```

运行可以得到：  
```r
JNIEnv->FindClass(com/wuaipojie/crackme2023/MainActivity) was called from RX@0x4000e310[lib52pojie.so]0xe310
JNIEnv->RegisterNatives(com/wuaipojie/crackme2023/MainActivity, RW@0x4006ac98[lib52pojie.so]0x6ac98, 1) was called from RX@0x4000e6e0[lib52pojie.so]0xe6e0
RegisterNative(com/wuaipojie/crackme2023/MainActivity, checkSn(Ljava/lang/String;Ljava/lang/String;)Z, RX@0x4000e830[lib52pojie.so]0xe830)
```
可以知道 checkSn 的偏移 0xe830  

构造参数调用 checkSn  
```java
package com.zj;

import com.github.unidbg.AndroidEmulator;
import com.github.unidbg.Module;
import com.github.unidbg.linux.android.AndroidEmulatorBuilder;
import com.github.unidbg.linux.android.AndroidResolver;
import com.github.unidbg.linux.android.dvm.DalvikModule;
import com.github.unidbg.linux.android.dvm.StringObject;
import com.github.unidbg.linux.android.dvm.VM;
import com.github.unidbg.memory.Memory;
import com.github.unidbg.virtualmodule.android.AndroidModule;

import java.io.File;
import java.util.ArrayList;
import java.util.List;

public class wuaipojie2023_2 {

    public static void main(String[] args) {
        AndroidEmulator emulator = AndroidEmulatorBuilder.for64Bit().setRootDir(new File("target/rootfs")).setProcessName("com.zj.wuaipojie2023_2").build();
        Memory memory = emulator.getMemory();
        memory.setLibraryResolver(new AndroidResolver(23));

        VM vm = emulator.createDalvikVM();
        vm.setVerbose(true);

        new AndroidModule(emulator, vm).register(memory);

        DalvikModule dm = vm.loadLibrary(new File("unidbg-android/src/test/java/com/zj/lib52pojie.so"), false);

        dm.callJNI_OnLoad(emulator);

        String uid = "12345678";
        String flag = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa";

        List<Object> list = new ArrayList<>();
        list.add(vm.getJNIEnv());
        list.add(0);
        list.add(vm.addLocalObject(new StringObject(vm, uid)));

        list.add(vm.addLocalObject(new StringObject(vm, flag)));

        Module module = dm.getModule();
        Number number = module.callFunction(emulator, 0xe830, list.toArray());
        System.out.println("result: " + number.intValue());
    }
}
```

运行可以得到：  
```r
JNIEnv->FindClass(com/wuaipojie/crackme2023/MainActivity) was called from RX@0x4000e310[lib52pojie.so]0xe310
JNIEnv->RegisterNatives(com/wuaipojie/crackme2023/MainActivity, RW@0x4006ac98[lib52pojie.so]0x6ac98, 1) was called from RX@0x4000e6e0[lib52pojie.so]0xe6e0
RegisterNative(com/wuaipojie/crackme2023/MainActivity, checkSn(Ljava/lang/String;Ljava/lang/String;)Z, RX@0x4000e830[lib52pojie.so]0xe830)
JNIEnv->GetStringUTFLength("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") was called from RX@0x4000f66c[lib52pojie.so]0xf66c
JNIEnv->GetStringUTFLength("12345678") was called from RX@0x4000f66c[lib52pojie.so]0xf66c
JNIEnv->GetStringUtfChars("12345678") was called from RX@0x4000f71c[lib52pojie.so]0xf71c
JNIEnv->GetStringUtfChars("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") was called from RX@0x4000e9e4[lib52pojie.so]0xe9e4
JNIEnv->ReleaseStringUTFChars("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") was called from RX@0x4000ec34[lib52pojie.so]0xec34
JNIEnv->ReleaseStringUTFChars("12345678") was called from RX@0x4000ecd4[lib52pojie.so]0xecd4
result: 0
```

学习了简单的unidbg使用，知道了怎么调用函数，其它的不会  
&&&&&&& 自己写的最简单的native程序连偏移都输不出来，还不知道为什么  


2023/3/8  
