# python3---pathlib

拼接路径, 找主目录什么的, 很方便  

```python
from pathlib import Path

home_dir = Path(__file__).parent
peid_signature_path = home_dir / 'data' / 'UserDB.TXT'
```

pathlib相应路径不是字符串，如果想转为字符串路径，直接 `str(home_dir)` 即可  


2019/12/10  
