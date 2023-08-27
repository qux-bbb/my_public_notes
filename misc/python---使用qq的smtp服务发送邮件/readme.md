# python---使用qq的smtp服务发送邮件

```python
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 设置邮箱的域名
HOST = "smtp.qq.com"

# 设置邮件标题
SUBJECT = "这是邮件标题"

# 设置邮件内容
CONTENT = "这是邮件内容"

# 设置发件人邮箱地址
FROM = "your_qq_email@qq.com"

# 设置收件人邮箱地址
TO = "recipient_email@example.com"

# 设置SMTP密码（这里需要使用QQ邮箱生成的授权码，而不是邮箱密码）
PASSWORD = "your_authorization_code"

# 设置邮件正文
message = MIMEText(CONTENT, "plain", "utf-8")
message["Subject"] = Header(SUBJECT, charset="utf-8")
message["From"] = Header(FROM)
message["To"] = Header(TO)

# 使用SSL连接
server = smtplib.SMTP_SSL(HOST)
server.connect(HOST, 465)
# 或者可以使用非SSL连接
# server = smtplib.SMTP(HOST)
# server.connect(HOST, 587)

# 登录邮箱
server.login(FROM, PASSWORD)

# 发送邮件
server.sendmail(FROM, TO, message.as_string())

# 关闭SMTP服务器
server.quit()

```


参考来源: chatgpt  


2023/8/27  
