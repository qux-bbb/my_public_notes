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
matches = rules.match(sample_path)
print(sample_path, matches)
```

加载多个yara文件的情况  
```python
import os
import yara

yara_rule_folder_path = "rules"

yara_filenames = os.listdir(yara_rule_folder_path)
yara_dict = {}
for yara_filename in yara_filenames:
    yara_path = os.path.join(yara_rule_folder_path, yara_filename)
    yara_dict[yara_filename] = yara_path
rules = yara.compile(filepaths=yara_dict)

sample_path = 'hello.txt'
matches = rules.match(sample_path)
print(matches)
print(matches[0].rule, matches[0].strings)
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

## 字符串计数
https://yara.readthedocs.io/en/stable/writingrules.html#counting-strings  
```r
rule CountExample
{
    strings:
        $a = "dummy1"
        $b = "dummy2"

    condition:
        #a == 6 and #b > 10
}
```

## 未匹配规则时输出匹配字段信息
```python
import yara


def mycallback(data):
    rule_name = data['rule']
    matched_string_names = data['strings']
    print(f"rule_name: {rule_name}, matched_string_names: {matched_string_names}")
    return yara.CALLBACK_CONTINUE


yara_rule_path = 'hello.yar'
rules = yara.compile(filepath=yara_rule_path)

sample_path = 'hello.txt'
matches = rules.match(sample_path, callback=mycallback, which_callbacks=yara.CALLBACK_NON_MATCHES)
print(sample_path, matches)
```

## 比较多的yara规则
https://github.com/Neo23x0/signature-base/tree/master/yara  
https://github.com/kevoreilly/CAPEv2/tree/master/data/yara/CAPE  
https://github.com/JPCERTCC/jpcert-yara  
https://github.com/Yara-Rules/rules/tree/master/malware  
https://github.com/ditekshen/detection/tree/master/yara  
