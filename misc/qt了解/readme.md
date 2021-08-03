# qt了解

## 简单信息
官网：https://www.qt.io/  
根据需要选择下载，下载比较坑爹的是需要先注册登录才能下载，把页面转成中文可能比较好找一些  
2020年开始，不提供离线安装包了，需要通过在线安装包下载安装，而且需要登录账号。  
qt统一的下载地址: https://download.qt.io/official_releases/  

可以从这里下载5.14之前的版本：  
http://mirrors.ustc.edu.cn/qtproject/official_releases/qt/5.14/5.14.2/  

简要介绍的地方--QT入门教程，就是大概做个了解  
http://c.biancheng.net/cpp/qt/  


## 简单的例子
Hello World窗口：main.cpp  
```cpp
#include <QApplication>
#include <QMainWindow>
#include <QLabel>
int main(int argc, char *argv[])
{
    QApplication app(argc, argv);
    QMainWindow w;
    w.setWindowTitle("Widgets演示");  //设置标题
    w.resize(300, 140);  //设置客户区大小
    QLabel label("Hello World!", &w);
    label.setGeometry(100, 50, 160, 30);
    w.show();
    return app.exec();
}
```

信号和槽演示：main.cpp  
```cpp
#include <QApplication>
#include <QMainWindow>
#include <QLabel>
#include <QPushButton>
#include <QLineEdit>
int main(int argc, char *argv[])
{
    QApplication app(argc, argv);
    QMainWindow w;
    w.setWindowTitle("Widget工程");
    w.resize(325, 120);
    QLineEdit lineEdit(&w);
    lineEdit.setGeometry(30, 20, 180, 36);
    lineEdit.setPlaceholderText("请输入文本");
    QPushButton btn("取消", &w);
    btn.setGeometry(220, 20, 70, 36);
    QLabel label(&w);
    label.setGeometry(30, 70, 250, 30);
    //连接clicke()信号和quit()槽
    QObject::connect(&btn, SIGNAL(clicked()), &app, SLOT(quit()));
    //连接textChanged()信号和setText()槽
    QObject::connect(&lineEdit, SIGNAL(textChanged(QString)), &label, SLOT(setText(QString)));
    w.show();
    return app.exec();
}
```


20201124  
