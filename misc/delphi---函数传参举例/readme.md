delphi函数是这么传参的：  
将前三个参数依次放入eax,edx,ecx，其他参数压栈，返回值是eax  

用来举例的代码：  
```delphi
program Project2;

{$APPTYPE CONSOLE}

uses
  SysUtils;

function add(num1:Integer; num2:Integer; num3:Integer; num4:Integer; num5:Integer; num6:Integer; num7:Integer; num8:Integer):Integer;
var
  sum:Integer;
begin
  sum:=num1+num2+num3+num4+num5+num6+num7+num8;
  result:=sum;
end;

var
  my_sum:Integer;
begin
  my_sum:=add(1,2,3,4,5,6,7,8);
  writeln(my_sum);
  readln;
end.
```

main函数一部分：  
```
CODE:00408331 push    4
CODE:00408333 push    5
CODE:00408335 push    6
CODE:00408337 push    7
CODE:00408339 push    8
CODE:0040833B mov     ecx, 3
CODE:00408340 mov     edx, 2
CODE:00408345 mov     eax, 1
CODE:0040834A call    sub_408294
CODE:0040834F mov     ebx, eax
```

add函数sub_408294：  
```
CODE:00408294 push    ebp
CODE:00408295 mov     ebp, esp
CODE:00408297 add     edx, eax
CODE:00408299 add     ecx, edx
CODE:0040829B add     ecx, [ebp+arg_10]
CODE:0040829E add     ecx, [ebp+arg_C]
CODE:004082A1 add     ecx, [ebp+arg_8]
CODE:004082A4 add     ecx, [ebp+arg_4]
CODE:004082A7 add     ecx, [ebp+arg_0]
CODE:004082AA mov     eax, ecx
CODE:004082AC pop     ebp
CODE:004082AD retn    14h
```


参考链接:   
1. https://blog.csdn.net/weixin_42528089/article/details/84189371
2. https://zhidao.baidu.com/question/1047654827959368259.html
