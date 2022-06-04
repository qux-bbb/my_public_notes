# python2---按行读文件判断结束

关键点在于判断
```python
# coding:utf8

poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
 use Python!
'''
f = open('poem.txt', 'w')  # open for 'w'riting
f.write(poem)  # write text to file
f.close()  # close the file
f = open('poem.txt')
# if no mode is specified, 'r'ead mode is assumed by default
while True:
    line = f.readline()
    if len(line) == 0:  # Zero length indicates EOF
        break
    print line,
 # Notice comma to avoid automatic newline added by Python
f.close()  # close the file
```


2018/1/31  
