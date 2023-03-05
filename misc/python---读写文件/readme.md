# python---读写文件

```python
# coding:utf8

file_path = "hello.txt"
the_content = "Hello World!"
the_file = open(file_path, "w")
the_file.write(the_content)
the_file.close()

the_file = open(file_path, "r")
content_read = the_file.read()
the_file.close()
print(content_read)

```

各种模式：  
| Character | Meaning                                                         |
| --------- | --------------------------------------------------------------- |
| 'r'       | open for reading (default)                                      |
| 'w'       | open for writing, truncating the file first                     |
| 'x'       | open for exclusive creation, failing if the file already exists |
| 'a'       | open for writing, appending to the end of file if it exists     |
| 'b'       | binary mode                                                     |
| 't'       | text mode (default)                                             |
| '+'       | open for updating (reading and writing)                         |


参考链接: https://docs.python.org/3/library/functions.html#open  


2023/3/5  
