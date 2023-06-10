# ajax---实时检测前台数据

```javascript
new Ajax().get("Send.asp?UserName="+val+"&t="+new Date().getTime(),
								function(R){
								s =R.responseText;
								if(s == 2){
								}else if(s == 1){
									alert('用户名 ' + val +' 已经被注册');
								}
						}); 
```

```
input的一个属性：
onBlur="CheckUser(this.value);"

当 <input> 字段失去焦点时发生 blur 事件
```


2017/9/2  
