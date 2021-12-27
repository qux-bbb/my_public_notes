# powershell---别名

powershell的命令有很多别名，目的是遵从习惯或方便输入吧。  

## 查询别名
`alias` 或 `get-alias`  

举例  
```r
> get-alias iex

CommandType     Name
-----------     ----
Alias           iex -> Invoke-Expression

> get-alias %

CommandType     Name
-----------     ----
Alias           % -> ForEach-Object
```


## 设置别名
`sal` 或 `Set-Alias`  

举例  
```r
sal hello write-host
```


2020/6/2  
