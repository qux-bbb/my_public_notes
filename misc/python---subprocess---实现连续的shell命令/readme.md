# python---subprocess---实现连续的shell命令

```sh
output=`dmesg | grep hda`
```

变成:  
```python
p1 = Popen(["dmesg"], stdout=PIPE)
p2 = Popen(["grep", "hda"], stdin=p1.stdout, stdout=PIPE)
p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
output = p2.communicate()[0]
```

摘自官方文档: https://docs.python.org/2.7/library/subprocess.html?highlight=subprocess#module-subprocess  


2020/4/2  
