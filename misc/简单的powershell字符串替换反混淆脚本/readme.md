# 简单的powershell字符串替换反混淆脚本

运行会调用powershell，有风险，如果是恶意脚本，请在虚拟机里使用  

```python
# python3
"""
@time: 2020/06/06
"""

import re
import subprocess

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


def main():
    test_file = open('test.txt')
    test_content = test_file.read()
    test_file.close()

    raw_strs = re.findall(r'\(".+?(?:-f)?.+?\)', test_content, re.IGNORECASE)

    for raw_str in raw_strs:
        cmd_list = ['powershell.exe', 'write-host', raw_str]
        status_code, output = subprocess_check_output(cmd_list)
        if status_code == 0:
            test_content = test_content.replace(raw_str, '("'+output.decode('utf8').strip()+'")')
        else:
            print(raw_str, status_code, output.decode('utf8'))
            exit(1)
    test_file = open('test_result.txt', 'w')
    test_file.write(test_content)
    test_file.close()

if __name__ == '__main__':
    main()
```


2020/6/6  
