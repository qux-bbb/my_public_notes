# python---解析xml

```python
import xml.etree.ElementTree as ET
tree = ET.parse('hello.xml')
result = tree.findtext('./file_info/malware')
```

2019/10/10  
