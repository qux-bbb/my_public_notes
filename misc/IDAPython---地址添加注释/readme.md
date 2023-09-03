# IDAPython---地址添加注释

keywords: ida python 添加注释  

自动批量给地址添加注释。  
第3个参数表示repeatable，1表示可重复，0表示不可重复。  

```python
import idaapi
import idc

addr_comment_dict = {
    0x004037AE: "ntdll.RtlInitUnicodeString",
    0x004038C9: "kernel32.IsWow64Process",
    # ... 其他地址和注释
}

print("开始添加注释...")

for addr, comment in addr_comment_dict.items():
    success = idc.set_cmt(addr, comment, 1)
    if success:
        print(f"地址 {hex(addr)} 添加注释 '{comment}' 成功!")
    else:
        print(f"地址 {hex(addr)} 添加注释 '{comment}' 失败!")

print("注释添加完成。")

```


来源: chatgpt  


2023/9/3  
