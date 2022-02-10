# python---解析googlenews的xml内容

```python
# coding:utf8

try:
    from io import BytesIO as StringIO
except ImportError:
    try:
        from cStringIO import StringIO
    except ImportError:
        from StringIO import StringIO

try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen

from pprint import pprint
from xml.etree import ElementTree

g = urlopen('http://news.google.com/news?topic=h&output=rss')
f= StringIO(g.read())
g.close()
tree = ElementTree.parse(f)
f.close()

def topnews(count=5):
    pair = [None, None]
    for elmt in tree.iter():
        if elmt.tag == 'title':
            skip = elmt.text.startswith('Top Stories')
            if skip:
                continue
            pair[0] = elmt.text
        if elmt.tag == 'link':
            if skip:
                continue
            pair[1] = elmt.text
            if pair[0] and pair[1]:
                count -= 1
                yield(tuple(pair))
                if not count:
                    return
                pair = [None, None]

for news in topnews():
    pprint(news)
```


2018/12/1  
