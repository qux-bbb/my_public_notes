# msidump

MSI Dump, 一个分析恶意MSI安装包、提取文件、流、二进制数据并结合YARA扫描的工具，仅限Windows系统安装使用。  
github地址: https://github.com/mgeeky/msidump  

## 安装
```r
git clone https://github.com/mgeeky/msidump.git
cd msidump
virtualenv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

## 使用示例

指定yar进行快速扫描  
```r
python msidump.py evil.msi -y rules.yara
```

提取可疑文件  
```r
python msidump.py evil2.msi -x binary -i lmskBju -O extracted
```
参数解释：  
- `-x binary` tells to extract contents of `Binary` table
- `-i lmskBju` specifies which record exactly to extract
- `-O extracted` sets output directory


## 参考链接
https://www.freebuf.com/articles/system/363055.html  


---
2023/5/3  
