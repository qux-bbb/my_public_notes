# Lazarus

keywords: Pascal  

Lazarus是一个兼容Delphi的跨平台IDE，用于快速应用程序开发。它有多种可供使用的组件和一个图形表单设计器，可以轻松创建复杂的图形用户界面。  

官网: https://www.lazarus-ide.org/index.php  

生成的exe开头是"MZ"，不是"MZP"  

## 设置整合窗口
Lazarus默认的各个窗口是分离的，没有简单的切换整合窗口的选项，可以安装anchordockingdsgn包重新编译IDE来解决  
```r
1. 包->安装/卸载包...
2. 选择右侧的"anchordockingdsgn 1.0"，点击"安装选择"
3. 点击下方的"保存并重新构建IDE"
4. 点击"继续"，等待即可  
```

https://blog.csdn.net/uijjuh_21/article/details/107883217  

## 简单的图形化程序示例
```r
unit Unit1;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls, Windows;

type

  { TForm1 }

  TForm1 = class(TForm)
    Button1: TButton;
    Edit1: TEdit;
    Edit2: TEdit;
    Label1: TLabel;
    Label2: TLabel;
    procedure Button1Click(Sender: TObject);
  private

  public

  end;

var
  Form1: TForm1;

implementation

{$R *.lfm}

{ TForm1 }

procedure TForm1.Button1Click(Sender: TObject);
var text1, text2: STRING;
begin
    text1:= Form1.Edit1.Text;
    text2:= Form1.Edit2.Text;
    Application.MessageBox(PChar('hello: '+text1+' '+text2), 'world', MB_OK);
end;

end.
```

## 一些缺点
1. 调试时不会自动显示一些变量的取值
2. 无法查看内存内容
3. 自动补全不大行


---
2022/1/20  
