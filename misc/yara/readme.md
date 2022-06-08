# yara

## 简单信息
yara，适用于恶意软件研究人员（及其他所有人）的模式匹配瑞士军刀。  

官网: https://virustotal.github.io/yara/  
github地址: https://github.com/VirusTotal/yara/  
文档地址: https://yara.readthedocs.io/en/stable/  

文档里有一些模块，可以使用比较高级的用法。  


## 安装
我主要用python，所以用pip安装  
```r
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
        pe.is_pe and $hello
}
```

`pe.is_pe` 和 `uint16(0) == 0x5A4D` 等价，如果需要判断是否为`MZ...PE`，可使用下面的逻辑  
```r
rule IsPE
{
    condition:
        // MZ signature at offset 0 and ...
        uint16(0) == 0x5A4D and
        // ... PE signature at offset stored in MZ header at 0x3C
        uint32(uint32(0x3C)) == 0x00004550
}
```

## 使用示例
```python
import yara

yara_rule_path = 'hello.yar'
rules = yara.compile(filepath=yara_rule_path)

sample_path = 'hello.txt'
result = rules.match(sample_path)
print(result)
```

加载多个yara文件的情况  
```python
yara_names = os.listdir(yara_rule_dir_path)
yara_dict = {}
for yara_name in yara_names:
    yara_path = os.path.join(yara_rule_dir_path, yara_name)
    yara_dict[yara_name] = yara_path
rules = yara.compile(filepaths=yara_dict)

sample_path = 'hello.txt'
result = rules.match(sample_path)
print(result)
```

## 精确偏移字符串匹配
https://yara.readthedocs.io/en/stable/writingrules.html#string-offsets-or-virtual-addresses  
```r
rule AtExample
{
    strings:
        $a = "dummy1"
        $b = "dummy2"

    condition:
        $a at 100 and $b at 200
}
```

不能直接把字符串写在condition里  


## 比较多的yara规则
https://github.com/Neo23x0/signature-base/tree/master/yara  
https://github.com/kevoreilly/CAPEv2/tree/master/data/yara/CAPE  
https://github.com/JPCERTCC/jpcert-yara  
https://github.com/Yara-Rules/rules/tree/master/malware  
https://github.com/ditekshen/detection/tree/master/yara  
