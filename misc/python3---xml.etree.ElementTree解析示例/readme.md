# python3---xml.etree.ElementTree解析示例

使用xml.etree.ElementTree解析xml文件示例  

示例xml文件: country_data.xml  
```xml
<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>
```

脚本：  
```python
import xml.etree.ElementTree as ET

tree = ET.parse('country_data.xml')
root = tree.getroot()

print('-'*80)
for child in root:
    print(child.tag, child.attrib)

print('-'*80)
print(root[0][1].text)

print('-'*80)
for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)

print('-'*80)
for country in root.findall('country'):
    rank = country.find('rank').text
    name = country.get('name')
    print(name, rank)
```

输出：  
```r
--------------------------------------------------------------------------------
country {'name': 'Liechtenstein'}
country {'name': 'Singapore'}
country {'name': 'Panama'}
--------------------------------------------------------------------------------
2008
--------------------------------------------------------------------------------
{'name': 'Austria', 'direction': 'E'}
{'name': 'Switzerland', 'direction': 'W'}
{'name': 'Malaysia', 'direction': 'N'}
{'name': 'Costa Rica', 'direction': 'W'}
{'name': 'Colombia', 'direction': 'E'}
--------------------------------------------------------------------------------
Liechtenstein 1
Singapore 4
Panama 68
```

使用iterparse解析xml大文件示例，效果比较好  
需要保证功能正确并且尽可能少地占用内存，clear的时机很重要  
```python
import xml.etree.ElementTree as ET

tree = ET.iterparse('country_data.xml')

element_to_clear = []
for event, element in tree:
    element_to_clear.append(element)
    if element.tag =='country':
        country_name = element.attrib.get('name', '')
        neighbors = element.findall('neighbor')
        neighbor_names = []
        for neighbor in neighbors:
            neighbor_names.append(neighbor.attrib.get('name', ''))
        print('-'*80)
        print(f'country_name: {country_name}')
        print(f'neighbors: {neighbor_names}')
        for ele in element_to_clear:  # 清理以减少内存使用
            ele.clear()
        element_to_clear.clear()
```


参考链接：  
1. https://docs.python.org/3.10/library/xml.etree.elementtree.html#tutorial
2. https://stackoverflow.com/questions/49245454/element-attributes-missing-when-parsing-xml-with-iterparse-lxml-python-2


2022/2/11  
