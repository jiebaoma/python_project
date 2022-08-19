import smtplib
from email.header import Header
from email.mime.text import MIMEText

smtpserver="smtp.163.com"
username="jiebaoma@163.com"
password="320826chen"
sender="jiebaoma@163.com"
receiver=["jiebaoma@126.com","1554491957@qq.com"]
subject="测试"
content="只是测试一下"

msg=MIMEText(content,"plain","utf-8")
msg["Subject"]=Header(subject,"utf-8")
msg["From"]=sender
msg["To"]=",".join(receiver)

try:
    smtp=smtplib.SMTP_SSL(smtpserver,465)
    smtp.helo(smtpserver)
    smtp.ehlo(smtpserver)
    smtp.login(username,password)
    smtp.sendmail(sender,receiver,msg.as_string())
    smtp.close()
    print("邮件发送成功....")
except Exception as e:
    print("邮件发送失败....")