# pip安装模块错误---NO_CERTIFICATE_OR_CRL_FOUND

pip 安装模块出现这样的错误：  
```r
hello@hello-VirtualBox:~/Desktop$ python3 -m pip install --upgrade pwntools
WARNING: Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLError(136, '[X509: NO_CERTIFICATE_OR_CRL_FOUND] no certificate or crl found (_ssl.c:4263)'))': /simple/pwntools/
WARNING: Retrying (Retry(total=3, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLError(136, '[X509: NO_CERTIFICATE_OR_CRL_FOUND] no certificate or crl found (_ssl.c:4263)'))': /simple/pwntools/
WARNING: Retrying (Retry(total=2, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLError(136, '[X509: NO_CERTIFICATE_OR_CRL_FOUND] no certificate or crl found (_ssl.c:4263)'))': /simple/pwntools/
WARNING: Retrying (Retry(total=1, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLError(136, '[X509: NO_CERTIFICATE_OR_CRL_FOUND] no certificate or crl found (_ssl.c:4263)'))': /simple/pwntools/
WARNING: Retrying (Retry(total=0, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLError(136, '[X509: NO_CERTIFICATE_OR_CRL_FOUND] no certificate or crl found (_ssl.c:4263)'))': /simple/pwntools/
Could not fetch URL https://pypi.org/simple/pwntools/: There was a problem confirming the ssl certificate: HTTPSConnectionPool(host='pypi.org', port=443): Max retries exceeded with url: /simple/pwntools/ (Caused by SSLError(SSLError(136, '[X509: NO_CERTIFICATE_OR_CRL_FOUND] no certificate or crl found (_ssl.c:4263)'))) - skipping
ERROR: Could not find a version that satisfies the requirement pwntools (from versions: none)
ERROR: No matching distribution found for pwntools
```

用如下命令重新装一遍pip：  
```r
python3 -m pip install --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org --upgrade pip
```

原链接：https://python-forum.io/Thread-Cannot-update-or-install-anything-with-pip-SSL-error  


2020/11/27  
