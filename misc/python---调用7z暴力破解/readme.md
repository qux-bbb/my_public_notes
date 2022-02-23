# python---调用7z暴力破解

先把7z添加到path里，然后就能用了，就是速度慢点，可以改成多线程  

```python
import subprocess

passwds = open("strings.txt",'r').read().split("\n")

for passwd in passwds:
    status_code = subprocess.call(['7z', 't', 'result.7z', '-p'+passwd])
    if status_code == 0:
        print("Get it: &" + passwd + "&")
        exit(0)
```

用 John the Ripper 就很快  


2018/4/12  
