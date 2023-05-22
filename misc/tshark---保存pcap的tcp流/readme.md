# tshark---保存pcap的tcp流

keywords: wireshark  

格式：  
```r
tshark -r <pcap_path> -qz follow,tcp,raw,<stream_number> > result
```

`raw` 会将数据保存为16进制字符串。  
数据行以"\t"开头为响应数据，否则为请求数据。请求数据不一定只有开始的1行或2行，响应数据后可能还有请求数据。  

除了 `raw` 还有别的取值：  
```r
ascii  ASCII output with dots for non-printable characters, 无法直接显示的字符会显示成"."
ebcdic EBCDIC output with dots for non-printable characters
hex    Hexadecimal and ASCII data with offsets, 左边16进制右边ascii，像十六进制编辑器的显示风格
raw    Hexadecimal data, 多个16进制字符串
yaml   YAML format
```

示例：  
```r
# 以raw格式保存tcp流0到result.data
tshark -r test.pcap -qz follow,tcp,raw,0 > result.data
```


2023/5/21  
