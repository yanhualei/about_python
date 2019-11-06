import smtplib
from email.mime.text import MIMEText
_user = "1147016165@qq.com"#发件人
_pwd = "hhvzrkmhnrfgicee"#qq邮箱授权码
_to = "1208832367@qq.com"#收件人

msg = MIMEText("Hellow,This is my first Email!")#邮件内容
msg["Subject"] = "come form xieolei!"#收件方显示的邮件主题
msg["From"] = _user#收件方显示的发件人
msg["To"] = _to#收件方显示的收件人

try:
	s = smtplib.SMTP_SSL("smtp.qq.com", 465)
	s.login(_user, _pwd)
	s.sendmail(_user, _to, msg.as_string())
	s.quit()
	print ("Success!")
except smtplib.SMTPException as e:
	print ("Falied,%s"%e)