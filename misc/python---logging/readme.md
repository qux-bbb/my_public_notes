# python---logging

python的日志模块logging简单使用。  

最初级用法，直接输出到控制台  
```python
# coding:utf8

import logging

# level设置为DEBUG可以全部显示，level越高显示越少
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

logging.debug('this is a loggging debug message')
logging.info('this is a loggging info message')
logging.warning('this is loggging a warning message')
logging.error('this is an loggging error message')
logging.critical('this is a loggging critical message')
```

输出到控制台和文件  
```python
# coding:utf8

import os
import sys
import logging

current_py_dir = os.path.dirname(os.path.abspath(__file__)) + '/'

app_name = 'AppName'

# 获取logger实例，如果参数为空则返回root logger
log = logging.getLogger(app_name)


def init_log():
    # 指定logger输出格式 -8s: 指定宽度为8，减号表示左对齐
    formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')

    # 文件日志，指定编码可以防止"UnicodeEncodeError"错误
    log_path = os.path.join(current_py_dir, f'{app_name}.log')
    file_handler = logging.FileHandler(log_path, encoding='utf8')
    file_handler.setFormatter(formatter)  # 可以通过setFormatter指定输出格式

    # 控制台日志
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    # console_handler.formatter = formatter  # 也可以直接给fomatter赋值

    # 为logger添加日志处理器，可以自定义日志处理器让其输出到其他地方
    log.addHandler(file_handler)
    log.addHandler(console_handler)

    # 指定日志的最低输出级别，默认为WARNING级别
    log.setLevel(logging.INFO)

    # # 移除一些日志处理器
    # log.removeHandler(file_handler)


def main():
    if len(sys.argv) != 2:
        print("usage: ...")
        return

    init_log()

    # 输出不同级别的log
    log.debug('this is debug info')
    log.info('this is information')
    log.warning('this is warning message')
    log.error('this is error message')
    log.fatal('this is fatal message, it is same as log.critical')
    log.critical('this is critical message')

if __name__ == '__main__':
    main()
```

如果要记录异常信息，可以在不同级别的log中加入参数：exc_info=1，如：  
`log.error('this is error message', exc_info=1)`  

注意:  
warn & warning  
warn被弃用，建议使用warning  

可以单独在一个文件里设置好log，其它文件直接import就可以用了  


参考：  
1. https://www.cnblogs.com/CJOKER/p/8295272.html
2. https://blog.csdn.net/hallo_ween/article/details/64906838
3. https://stackoverflow.com/questions/52896485/python3-logger-unicodeencodeerror
