import smtplib
from email.mime.text import MIMEText

msg_from = '2403818207@qq.com'  # 发送方邮箱
passwd = 'breqotnlohvlecgf'  # 填入发送方邮箱的授权码
msg_to = '1798388726@qq.com'  # 收件人邮箱

subject = "python邮件测试"  # 主题
content = "这是我使用python smtplib及email模块发送的邮件"# 正文
msg = MIMEText(content)
msg['Subject'] = subject
msg['From'] = msg_from
msg['To'] = msg_to
s = smtplib.SMTP_SSL("smtp.qq.com", 465)# 邮件服务器及端口号
s.login(msg_from, passwd)
s.sendmail(msg_from, msg_to, msg.as_string())
s.quit()