# frida---js模板

hook.js  
```javascript
//定义一个名为hookTest1的函数
function hookTest1() {
    //获取一个名为"类名"的Java类，并将其实例赋值给JavaScript变量utils
    var utils = Java.use("类名");
    //修改"类名"的"method"方法的实现。这个新的实现会接收两个参数（a和b）
    utils.method.implementation = function (a, b) {
        //将参数a和b的值改为123和456。
        a = 123;
        b = 456;
        //调用修改过的"method"方法，并将返回值存储在`retval`变量中
        var retval = this.method(a, b);
        //在控制台上打印参数a，b的值以及"method"方法的返回值
        console.log(a, b, retval);
        //返回"method"方法的返回值
        return retval;
    }
}

function main() {
    Java.perform(function () {
        hookTest1();
    });
}
setImmediate(main);
```

setImmediate是为了防止超时  


内容来源: https://www.52pojie.cn/thread-1823118-1-1.html  


2024/5/26  
