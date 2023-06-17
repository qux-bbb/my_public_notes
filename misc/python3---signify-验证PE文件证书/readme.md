# python3---signify-验证PE文件证书

keywords: 验证签名  

signify可以用来查看和验证PE文件证书  
github地址: https://github.com/ralphje/signify  

安装模块：  
```r
pip install signify
```

示例：  
```python
from signify.authenticode.signed_pe import SignedPEFile

with open("Everything.exe", "rb") as f:
    try:
        pe = SignedPEFile(f)
        for signed_data in pe.signed_datas:
            print("Included certificates:")
            for cert in signed_data.certificates:
                print(f"    Subject: {cert.subject.dn}")
                print(f"    Issuer: {cert.issuer.dn}")
                print(f"    Serial: {cert.serial_number}")
                print(f"    Valid from: {cert.valid_from}")
                print(f"    Valid to: {cert.valid_to}")

            print()
            print("Signer:")
            print(f"    Issuer: {signed_data.signer_info.issuer.dn}")
            print(f"    Serial: {signed_data.signer_info.serial_number}")
            print(f"    Program name: {signed_data.signer_info.program_name}")
            print(f"    More info: {signed_data.signer_info.more_info}")

            if signed_data.signer_info.countersigner:
                countersigner = signed_data.signer_info.countersigner
                print()
                print("Countersigner:")
                print(f"    Issuer: {countersigner.signer_info.issuer.dn}")
                print(f"    Serial: {countersigner.signer_info.serial_number}")
                print(f"    Signing time: {countersigner.signing_time}")

            print()
            try:
                signed_data.verify()
                print("Signature: valid")
            except Exception as e:
                print("Signature: invalid")
                print(f"{e}")

    except Exception as e:
        print("Error while parsing: " + str(e))
```

输出：  
```r
Included certificates:
    Subject: CN=voidtools, O=voidtools, L=Wilmington, ST=South Australia, C=AU
    Issuer: CN=DigiCert SHA2 Assured ID Code Signing CA, OU=www.digicert.com, O=DigiCert Inc, C=US
    Serial: 19513861298539538856767452546965809223
    Valid from: 2020-11-16 00:00:00+00:00
    Valid to: 2022-03-17 23:59:59+00:00
    Subject: CN=DigiCert SHA2 Assured ID Code Signing CA, OU=www.digicert.com, O=DigiCert Inc, C=US
    Issuer: CN=DigiCert Assured ID Root CA, OU=www.digicert.com, O=DigiCert Inc, C=US
    Serial: 5364131601516814570659357524942475272
    Valid from: 2013-10-22 12:00:00+00:00
    Valid to: 2028-10-22 12:00:00+00:00

Signer:
    Issuer: CN=DigiCert SHA2 Assured ID Code Signing CA, OU=www.digicert.com, O=DigiCert Inc, C=US
    Serial: 19513861298539538856767452546965809223
    Program name: None
    More info: None

Countersigner:
    Issuer: CN=DigiCert SHA2 Assured ID Timestamping CA, OU=www.digicert.com, O=DigiCert Inc, C=US
    Serial: 17624174242159194906345698804472279261
    Signing time: 2021-01-25 06:38:24+00:00

Signature: valid
```


2019/12/3  
