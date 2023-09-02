# IDAPython---未识别函数创建

keywords: ida python 创建函数  

有时候IDA不能自动识别一些函数，指令都是红色的，虽然可以自己一个个创建函数，但是太慢了，所以用脚本实现一下，创建有明显开头特征的函数。  

```python
import idautils
import idc
import idaapi
import ida_search

print("脚本开始执行")

# "push ebp" 的机器码是 55
# "mov ebp, esp" 的机器码是 8B EC
combined_pattern = "55 8B EC"

# 遍历所有的代码段
for seg_ea in idautils.Segments():
    # 获取段的名称
    seg_name = idc.get_segm_name(seg_ea)
    print(f"正在搜索代码段：{seg_name}")

    # 检查该段是否包含指令
    seg_type = idc.get_segm_attr(seg_ea, idc.SEGATTR_TYPE)
    if seg_type != idaapi.SEG_CODE:
        continue

    # 获取段的结束地址
    seg_end = idc.get_segm_end(seg_ea)

    not_found = True  # 用于跟踪是否找到目标模式

    # 在该段内搜索
    ea = seg_ea
    while ea < seg_end:
        # 使用 ida_search.find_binary 搜索组合的指令模式
        ea = ida_search.find_binary(ea, seg_end, combined_pattern, 16, idc.SEARCH_DOWN)
        if ea == idaapi.BADADDR:
            if not_found:
                print(f"在代码段 {seg_name} 中未找到目标模式")
            break  # 未找到

        not_found = False  # 找到了目标模式

        # 检查是否已经是一个函数
        if idaapi.get_func(ea):
            print(f"地址 0x{ea:X} 已经是一个函数，跳过")
        else:
            # 如果找到匹配，尝试创建函数
            if not idaapi.add_func(ea):
                print(f"在代码段 {seg_name} 的 0x{ea:X} 位置无法创建函数")
            else:
                print(f"在代码段 {seg_name} 的 0x{ea:X} 位置成功创建函数")

        # 更新地址以继续搜索
        ea = idc.next_head(ea, seg_end)

print("脚本执行完毕")

```

来源: chatgpt  


2023/9/3  
