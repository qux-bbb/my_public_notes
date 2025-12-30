# IDA---导出数据到文件

## 少量数据
直接选中，Edit -> Export data(快捷键Shift+E) 导出数据即可

## 大量数据

### 方法1
```r
Edit -> Begin selection(快捷键Alt+L) 开始选择
Jump -> Jump to address...(快捷键G)使用绝对地址或相对地址跳转，确定选择范围
Edit -> Export data(快捷键Shift+E) 导出数据即可
# 如果想取消选择，Edit -> Abort selection(快捷键Alt+L)
# 记住快捷键后操作很快
```

### 方法2
```python
# 左下角切换为Python，粘贴回车即可
# 或者 File -> Script command...，语言切换为Python，粘贴运行即可
import ida_bytes

ea = 0x0000000140004428 # 起始地址
size = 300 # 字节数
output_file = "dump.bin"

# 读取原始字节
data = ida_bytes.get_bytes(ea, size)

if data and len(data) == size:
    with open(output_file, "wb") as f:
        f.write(data)
    print(f"[+] 成功导出 {size} 字节到 {output_file}")
else:
    print(f"[-] 无法读取 {size} 字节数据（可能超出段边界）")

```
