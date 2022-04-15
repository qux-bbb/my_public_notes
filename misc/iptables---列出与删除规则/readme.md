# iptables---列出与删除规则

```r
# --verbose -v, 展示更多细节
# --numeric -n, 数字化展示地址，比较快
# --list -L, 列出一条链或所有链的规则
# --line-numbers, 带行号
# 常用的一个命令，列出链上所有规则，包括细节，数字化展示地址，带行号
iptables -vnL --line-numbers

# 从列出的规则中选择一行删除，下面的命令会删除FORWARD链中的第1条规则  
iptables -D FORWARD 1

# 清除所有规则
iptables -F
```

2018/11/8  
