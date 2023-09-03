# IDAPython---地址添加标签

keywords: ida python 添加标签  

自动批量给地址添加标签，错误时可以将相应地址数据定义清掉再执行一遍脚本试试。  

```python
import idc

# 地址和标签的字典
address_label_dict = {
    0x002E0268: "user32.MessageBoxA",
    0x002E0270: "user32.FindWindowA",
    0x002E0278: "user32.GetWindowThreadProcessId"
}

# 给地址添加标签
def add_label(address, label):
    if idc.set_name(address, label, idc.SN_NOWARN):
        print(f"成功：为地址 {hex(address)} 添加标签 {label}")
    else:
        print(f"失败：无法为地址 {hex(address)} 添加标签 {label}")

print("脚本开始执行")
# 使用循环为所有地址添加标签
for address, label in address_label_dict.items():
    add_label(address, label)
print("脚本执行完毕")
```


来源: chatgpt  


2023/9/3  
