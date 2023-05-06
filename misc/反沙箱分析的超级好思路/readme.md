# 反沙箱分析的超级好思路

在真正做事之前，做大量无用循环，循环里加一些沙箱可能会hook的api，这样可以很大程度延缓执行速度，让沙箱超时终止  

也不是真正的完全无用循环，等于特定值时，做一些有意义的操作即可  

举例:  
```c++
int a = 1;

for(int i = 0; i < 99999999; i++){
    // call some api
    GetSystemInfo();
    if(i==9999){
        // do some useful but not important thing
        a = 99;
    }
}

// do important thing
if(a==99){
    cout << "We got the right num!" << endl;
}else{
    // do some fake thing or do nothing
    exit(0)
}

```


2019/8/27  
