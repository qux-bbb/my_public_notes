Beautiful Soup 是一个可以从HTML或XML文件中提取数据的Python库  
官方文档: https://beautifulsoup.readthedocs.io/  
安装: `pip install beautifulsoup4`  

使用示例：  
```python
# coding:utf8
# python3

from bs4 import BeautifulSoup


html_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Test</title>
</head>
<body>
    <h1>Hello</h1>
    <p>1</p>
    <p id="key_content">You find me by id!</p>
    <p class="key_content">You find me by class!</p>
    <p>1</p>
    <img src="http://hello.com/contents/imgs/12345/6789.jpg" alt="cat play boll">
    <a class="link_to_article" href="/date/20211202/">
        <div>
            <p>Today is a happy day</p>
        </div>
    </a>
    <a class="link_to_article" href="/date/20211203/">
        <div>
            <p>Today is a bad day</p>
        </div>
    </a>
</body>
</html>
'''

soup = BeautifulSoup(html_content, 'html.parser')

# find by id
print('find by id')
the_id_p = soup.find('p', id='key_content')
print('the_id_p content: {}\n'.format(the_id_p.string))

# find by class
print('find by class')
the_class_p = soup.find('p', class_='key_content')
print('the_class_p content: {}\n'.format(the_class_p.string))

# get attribute
print('get attribute')
the_img = soup.find('img')
print('the_img info src: {}, alt: {}\n'.format(the_img.get('src'), the_img.get('alt')))

# get element value
print('get element value')
some_a = soup.find_all('a', class_='link_to_article')
for the_a in some_a:
    print('href: {}, info: {}'.format(the_a.get('href'), the_a.div.p.string))

```
