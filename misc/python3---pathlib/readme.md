# python3---pathlib

拼接路径, 找主目录什么的, 很方便  

```python
from pathlib import Path

home_dir = Path(__file__).resolve().parent
peid_signature_path = home_dir / 'data' / 'UserDB.TXT'
```

resolve 可以转绝对路径，解析符号链接，路径标准化。  

pathlib相应路径不是字符串，如果想转为字符串路径，直接 `str(home_dir)` 即可  


2019/12/10  
