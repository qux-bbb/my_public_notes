# python---subprocess.check_output封装

subprocess.check_output函数执行命令出现错误会抛出异常，这里简单封装一下，return返回值和输出。  

```python
def subprocess_check_output(cmd_list):
    """封装 check_output
    返回returncode和output
    cmd_list举例: cmd_list = ['dir', 'D:/']
    """
    try:
        output = subprocess.check_output(cmd_list, stderr=subprocess.STDOUT)
        return 0, output
    except Exception as e:
        return e.returncode, e.output
```

2020/4/1  
