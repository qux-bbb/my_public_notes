# python---chardet

chardet用于检测编码，内容长的时候才好用。  

安装：  
```r
pip install chardet
```

示例：  
```python
import urllib.request
import chardet

rawdata = urllib.request.urlopen('http://yahoo.co.jp/').read()
result = chardet.detect(rawdata)
print(result)
```
输出：  
```r
{'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}
```

2019/8/19  
