# XLMMacroDeobfuscator

keywords: macro4.0  

XLMMacrodeobfousator可用于解码混淆的XLM宏（也称为Excel 4.0宏）。  
原理是利用内部XLM仿真器来解释宏，不是完全执行代码。  

支持xls、xlsm和xlsb格式。  

github地址: https://github.com/DissectMalware/XLMMacroDeobfuscator  

安装：  
```r
pip install XLMMacroDeobfuscator --force
```

使用：  
```r
# 提取并做反混淆
xlmdeobfuscator --file document.xlsm
# 只提取不做反混淆
xlmdeobfuscator --file document.xlsm -x
# 结果保存为json格式
xlmdeobfuscator --file document.xlsm --export-json result.json
```


2022/1/17  
