# python---解析windows事件日志

安装模块：  
```r
pip install python-evtx
```

简单解析脚本：  
```python
# coding:utf8

import mmap
import contextlib

from Evtx.Evtx import FileHeader
from Evtx.Views import evtx_file_xml_view


def MyFun():
    EvtxPath = "C:/Users/hello/Desktop/test.evtx"  # 日志文件的路径

    with open(EvtxPath, "r") as f:
        with contextlib.closing(
            mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        ) as buf:
            fh = FileHeader(buf, 0)
            # 构建一个xml文件，根元素是Events
            print("")
            print("")
            # 遍历事件
            for xml, record in evtx_file_xml_view(fh):
                print("=" * 80)
                print(xml)
            print("")


if __name__ == "__main__":
    MyFun()
```

原链接：https://www.colabug.com/2622614.html  


2019/4/14  
