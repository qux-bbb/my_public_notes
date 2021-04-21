# 自建CA生成证书并签名

搜索 makecert.exe, 将其所在文件夹路径添加到path环境变量  
新建文件夹for_sign，打开命令行切换目录到该文件夹，执行以下命令生成相关证书：  
```bat
:: windows下执行
makecert -r -pe -n "CN=Test CA" -ss CA -sr CurrentUser -a sha256 -cy authority -sky signature -sv TestCA.pvk TestCA.cer
:: certutil -user -addstore Root TestCA.cer
makecert -pe -n "CN=Test Cert" -a sha256 -cy end -sky signature -ic TestCA.cer -iv TestCA.pvk -sv TestCert.pvk TestCert.cer
pvk2pfx -pvk TestCert.pvk -spc TestCert.cer -pfx TestCert.pfx
```
弹出设置密码时选择"无"  

将可执行程序复制到for_sign文件夹，执行以下命令进行签名：  
```bat
signtool sign /v /f TestCert.pfx /t http://timestamp.sectigo.com Test.exe
```

签名后即可使用，不过由于CA是自己生成的，查看证书会显示根证书不可信  

签名时的`/t`选项后跟时间戳服务器，时间戳服务器可能会签名失败，可以换几个，实测`http://timestamp.sectigo.com`可用  
```
http://tsa.starfieldtech.com
http://timestamp.globalsign.com/scripts/timstamp.dll
http://timestamp.comodoca.com/authenticode
http://www.startssl.com/timestamp
http://timestamp.verisign.com/scripts/timstamp.dll
http://timestamp.sectigo.com
```


2021/4/16
