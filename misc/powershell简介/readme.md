# powershell简介

PowerShell 是一种跨平台的任务自动化解决方案，由命令行 shell、脚本语言和配置管理框架组成。  
PowerShell 可以在 Windows、Linux 和 macOS 上运行。  

## 流程控制
```r
# foreach
$ComputerName = 'DC01', 'WEB01'
foreach ($Computer in $ComputerName) {
  Get-ADComputer -Identity $Computer
}

# for
for ($i = 1; $i -lt 5; $i++) {
  Write-Output "Sleeping for $i seconds"
  Start-Sleep -Seconds $i
}

# do util
$number = Get-Random -Minimum 1 -Maximum 10
do {
  $guess = Read-Host -Prompt "What's your guess?"
  if ($guess -lt $number) {
    Write-Output 'Too low!'
  }
  elseif ($guess -gt $number) {
    Write-Output 'Too high!'
  }
}
until ($guess -eq $number)

# do while
$number = Get-Random -Minimum 1 -Maximum 10
do {
  $guess = Read-Host -Prompt "What's your guess?"
  if ($guess -lt $number) {
    Write-Output 'Too low!'
  } elseif ($guess -gt $number) {
    Write-Output 'Too high!'
  }
}
while ($guess -ne $number)

# while
$date = Get-Date -Date 'November 22'
while ($date.DayOfWeek -ne 'Thursday') {
  $date = $date.AddDays(1)
}
Write-Output $date

# break 中断循环
for ($i = 1; $i -lt 5; $i++) {
  Write-Output "Sleeping for $i seconds"
  Start-Sleep -Seconds $i
  break
}

# continue 跳到循环的下一迭代
while ($i -lt 5) {
  $i += 1
  if ($i -eq 3) {
    continue
  }
  Write-Output $i
}

# return 退出现有作用域
$number = 1..10
foreach ($n in $number) {
  if ($n -ge 4) {
    Return $n
  }
}
```


## 函数
```r
# 普通函数
function Get-PSVersion {
    $PSVersionTable.PSVersion
}

# 带参数的函数
function Test-MrParameter {

    param (
        $ComputerName
    )

    Write-Output $ComputerName

}

# 带默认参数的函数
function Test-MrDefaultParameter {

    param (
        $ComputerName = $env:COMPUTERNAME
    )

    Write-Output $ComputerName

}
```


## 原链接
1. https://learn.microsoft.com/zh-cn/powershell/scripting/overview
2. https://learn.microsoft.com/zh-cn/powershell/scripting/learn/ps101/00-introduction


---
2022/12/4  
