# angr---4种state

简介
===

state，程序状态，从源码看大概有4种state，这里简单摘抄一下，具体信息去看源码注释  

使用方式举例：  
`project.factory.blank_state()`  


blank_state
-----------
```
Returns a mostly-uninitialized state object. All parameters are optional.
```
```
返回一个大部分未初始化的状态对象。所有参数都是可选的。
```


entry_state
-----------
```
Returns a state object representing the program at its entry point. All parameters are optional.
```
```
返回表示程序入口点的状态对象。所有参数都是可选的。
```


full_init_state
---------------
```
Very much like :meth:`entry_state()`, except that instead of starting execution at the program entry point,
execution begins at a special SimProcedure that plays the role of the dynamic loader, calling each of the 
initializer functions that should be called before execution reaches the entry point.
```
```
和`entry_state()`很像，不是从程序入口点，而是从一个特殊的SimProcedure开始执行，
该SimProcedure扮演动态加载程序的角色，调用在到达入口点之前应该调用的每个初始值设定项函数。
```


call_state
----------
```
Returns a state object initialized to the start of a given function, as if it were called with given parameters.
```
```
返回在给定函数开始时初始化的状态对象，就像使用给定参数调用它一样。
```


2020/8/9  
