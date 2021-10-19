## 简单信息
yara，适用于恶意软件研究人员（及其他所有人）的模式匹配瑞士军刀。  

官网: https://virustotal.github.io/yara/  
github地址: https://github.com/VirusTotal/yara/  
文档地址: https://github.com/VirusTotal/yara/  

文档里有一些模块，可以使用比较高级的用法。  


## 安装
我主要用python，所以用pip安装  
```
pip install yara-python
```


## yara规则示例
hello.yar  
```r
import "pe"

rule hello_world {
    meta:
        description = "Detect hello world in pe"
        author = "alice"
        date = "2021-10-19"
        hash1 = "d15a99eb7d9b3ad44883ae7679a52769"
    strings:
        $hello = "Hello World"
    condition:
        pe.is_pe() and $hello
}
```

## 使用示例
```python
import yara

yara_rule_path = 'hello.yar'
rules = yara.compile(filepath=yara_rule_path)

result = rules.match(sample_path)
```

加载多个yara文件的情况  
```python
yara_names = os.listdir(yara_rule_dir_path)
yara_dict = {}
for yara_name in yara_names:
    yara_path = os.path.join(yara_rule_dir_path, yara_name)
    yara_dict[yara_name] = yara_path
rules = yara.compile(filepaths=yara_dict)

result = rules.match(sample_path)
```
