# python3---pathlib

pathlib是python3.4的新模块，拼接路径, 找主目录什么的, 很方便  

官方文档: https://docs.python.org/zh-cn/3/library/pathlib.html  

```python
from pathlib import Path

# resolve 可以转绝对路径，解析符号链接，路径标准化
home_dir = Path(__file__).resolve().parent
peid_signature_path = home_dir / 'data' / 'UserDB.TXT'
```

遍历文件夹：  
```python
from pathlib import Path

the_folder_path = Path("test_folder")
for the_path in the_folder_path.iterdir():
    the_name = the_path.name
    if the_name in (".idea", ".vscode"):
        continue
    print(the_path)
```

指定模式遍历文件夹：  
```python
from pathlib import Path

the_folder_path = Path("test_folder")

for the_path in the_folder_path.glob(r"*.txt"):
    the_name = the_path.name
    if the_name in (".idea", ".vscode"):
        continue
    print(the_path)
```


pathlib相应路径不是字符串，如果想转为字符串路径，直接 `str(home_dir)` 即可  


2019/12/10  
