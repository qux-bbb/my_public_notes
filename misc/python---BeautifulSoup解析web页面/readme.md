# python---BeautifulSoup解析web页面

```r
pip install BeautifulSoup
```

```python
# coding:utf8

from HTMLParser import HTMLParser
from cStringIO import StringIO
from urllib2 import urlopen
from urlparse import urljoin

from BeautifulSoup import BeautifulSoup, SoupStrainer

URLs = (
    'http://python.org',
    'https://cn.bing.com',
)

def output(x):
    print '\n'.join(sorted(set(x)))

def simpleBS(url, f):
    'simpleBS() - use BeautifulSoup to parse all tags to get anchors'
    output(urljoin(url, x['href']) for x in BeautifulSoup(f).findAll('a'))

def fasterBS(url, f):
    'fasterBS() - use BeautifulSoup to parse only anchor tags'
    output(urljoin(url, x['href']) for x in BeautifulSoup(f, parseOnlyThese=SoupStrainer('a')))

def htmlparser(url, f):
    'htmlparse() - use HTMLParser to parse anchor tags'
    class AnchorParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            if tag != 'a':
                return
            if not hasattr(self, 'data'):
                self.data = []
            for attr in attrs:
                if attr[0] == 'href':
                    self.data.append(attr[1])
    parser = AnchorParser()
    parser.feed(f.read())
    output(urljoin(url, x) for x in parser.data)


def process(url, data):
    print '\n*** simple BS'
    simpleBS(url, data)
    data.seek(0)
    print '\n*** faster BS'
    fasterBS(url, data)
    data.seek(0)
    print '\n*** HTMLParser'
    htmlparser(url, data)

def main():
    for url in URLs:
        f = urlopen(url)
        data = StringIO(f.read())
        f.close()
        process(url, data)

if __name__ == '__main__':
    main()
```


2018/11/15  
