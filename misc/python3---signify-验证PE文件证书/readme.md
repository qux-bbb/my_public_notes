# python3---signify-验证PE文件证书

keywords: 验证签名  

```python
from signify.signed_pe import SignedPEFile

with open('Everything.exe', 'rb') as f:
    try:
        pe = SignedPEFile(f)
        for signed_data in pe.signed_datas:
            print("    Included certificates:")
            for cert in signed_data.certificates:
                print("      - Subject: {}".format(cert.subject_dn))
                print("        Issuer: {}".format(cert.issuer_dn))
                print("        Serial: {}".format(cert.serial_number))
                print("        Valid from: {}".format(cert.valid_from))
                print("        Valid to: {}".format(cert.valid_to))

            print()
            print("    Signer:")
            print("        Issuer: {}".format(signed_data.signer_info.issuer_dn))
            print("        Serial: {}".format(signed_data.signer_info.serial_number))
            print("        Program name: {}".format(signed_data.signer_info.program_name))
            print("        More info: {}".format(signed_data.signer_info.more_info))

            if signed_data.signer_info.countersigner:
                print()
                print("    Countersigner:")
                print("        Issuer: {}".format(signed_data.signer_info.countersigner.issuer_dn))
                print("        Serial: {}".format(signed_data.signer_info.countersigner.serial_number))
                print("        Signing time: {}".format(signed_data.signer_info.countersigner.signing_time))

            print()
            try:
                signed_data.verify()
                print("    Signature: valid")
            except Exception as e:
                print("    Signature: invalid")
                print("    {}".format(e))

    except Exception as e:
        raise
        print("    Error while parsing: " + str(e))
```


2019/12/3  
