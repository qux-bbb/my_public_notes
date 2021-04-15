windows很多api的参数在msdn上都是常量名，没有对应的值  
而逆向时只能看到值，不知道对应的常量名  

现在能想到的方法是，自己装一个vs，然后照着msdn写对应的函数，这样可以跟踪到相应的头文件，就有常量名和数字的对应关系了  

上面方法有点麻烦，这个插件很好用: https://github.com/ThunderCls/xAnalyzer/  
数据是根据windows sdk header文件生成的  
在x64dbg里，右键 -> xAnalyzer -> Analyze Function, 就能看到值对应的常量名了  
如果想自己去搜，可以在这里搜: https://github.com/ThunderCls/xAnalyzer/tree/master/apis_def  