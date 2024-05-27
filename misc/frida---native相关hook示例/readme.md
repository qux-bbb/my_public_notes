# frida---native相关hook示例

整数型修改：  
```javascript
function hookTest3(){
    Java.perform(function(){
        //根据导出函数名打印地址
        var helloAddr = Module.findExportByName("lib52pojie.so","func_four");
        console.log(helloAddr);
        if(helloAddr != null){
            Interceptor.attach(helloAddr,{
                onEnter: function(args){  //args参数
                    args[0] = ptr(1000); //第一个参数修改为整数 1000，先转为指针再赋值
                    console.log(args[0]);
                      
                },
                onLeave: function(retval){  //retval返回值
                    retval.replace(20000);  //返回值修改
                    console.log("retval",retval.toInt32());
                }
            })
        }
    })
}
```

字符串类型修改：  
```javascript
function hookTest2(){
    Java.perform(function(){
        //根据导出函数名打印地址
        var helloAddr = Module.findExportByName("lib52pojie.so","Java_com_zj_wuaipojie_util_SecurityUtil_vipLevel");
        if(helloAddr != null){
            Interceptor.attach(helloAddr,{
                //onEnter里可以打印和修改参数
                onEnter: function(args){  //args传入参数
                    var JNIEnv = Java.vm.getEnv();
                    var originalStrPtr = JNIEnv.getStringUtfChars(args[2], null).readCString();	
                    console.log("参数:", originalStrPtr);
                    var modifiedContent = "至尊";
                    var newJString = JNIEnv.newStringUtf(modifiedContent);
                    args[2] = newJString;				
                },
                //onLeave里可以打印和修改返回值
                onLeave: function(retval){  //retval返回值
                    var returnedJString = Java.cast(retval, Java.use('java.lang.String'));
                    console.log("返回值:", returnedJString.toString());
                    var JNIEnv = Java.vm.getEnv();
                    var modifiedContent = "无敌";
                    var newJString = JNIEnv.newStringUtf(modifiedContent);
                    retval.replace(newJString);
                }
            })
        }
    })
}
```

api地址: https://frida.re/docs/javascript-api/  

脚本来源: https://github.com/ZJ595/AndroidReverse/blob/main/Article/15%E7%AC%AC%E5%8D%81%E4%BA%94%E8%AF%BE%E3%80%81%E6%98%AF%E6%97%B6%E5%80%99%E5%AD%A6%E4%B9%A0%E4%B8%80%E4%B8%8BFrida%E4%B8%80%E6%8A%8A%E6%A2%AD%E4%BA%86(%E4%B8%8B).md  


2024/5/27  
