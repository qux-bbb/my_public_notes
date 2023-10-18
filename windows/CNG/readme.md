# CNG

CNG, CryptoAPI Next Generation, 用来计算hash、对数据签名、加密解密数据等。  

SHA256示例: [CNG_SHA256_TEST.cpp](files/CNG_SHA256_TEST.cpp)  
SHA256示例输出: [CNG_SHA256_TEST_output.txt](files/CNG_SHA256_TEST_output.txt)  

AES示例: [CNG_AES_TEST.cpp](files/CNG_AES_TEST.cpp)  
AES示例输出: [CNG_AES_TEST_output.txt](files/CNG_AES_TEST_output.txt)  

RC4示例(根据AES代码改的): [CNG_RC4_TEST.cpp](files/CNG_RC4_TEST.cpp)  
RC4示例输出: [CNG_RC4_TEST_output.txt](files/CNG_RC4_TEST_output.txt)  

RSA  
```r
流程：
1. 生成密钥对，写入文件
2. 写raw.txt
3. 读公钥，加密数据
4. 读私钥，解密数据

导出的公钥文件以"RSA1"开头，私钥文件以"RSA2"开头，私钥文件中包含公钥

注意：加密时选择填充方式 BCRYPT_PAD_PKCS1，不填充的话，只能加密很小的部分，具体见 social.msdn.microsoft.com 的参考链接
```
RSA示例: [CNG_RSA_TEST.cpp](files/RSA_files/CNG_RSA_TEST.cpp)  
RSA示例输出: [CNG_RSA_TEST_output.txt](files/RSA_files/CNG_RSA_TEST_output.txt)  


参考链接：  
1. https://learn.microsoft.com/zh-cn/windows/win32/seccng/cng-portal
2. https://www.drmaster.com.tw/Bookinfo.asp?BookID=MP21930
3. https://download.drmaster.com.tw/download/example/MP21930_Example.zip
4. https://stackoverflow.com/a/58426210/7164926
5. https://social.msdn.microsoft.com/Forums/windowsdesktop/en-US/007a0e26-7fc0-4079-9b63-2ad23f866836/bug-in-rsa-encryptiondecryption-using-cng?forum=windowssdk


2022/11/6  
