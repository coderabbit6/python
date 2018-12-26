from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr
import smtplib
# def _format_addr(s):
# 	name,addr = parseaddr(s)
# 	return formataddr((Header(name,'utf-8').encode(),addr))
from_addr = 'a2416841692@163.com'
password = 'scp142857'
to_addr = '1424626893@qq.com'
# to_addr = '1807612723@qq.com'
# to_addr = '415852926@qq.com'
smtp_server = 'smtp.163.com'

msg = MIMEText("python网络爬虫运行出错，请及时调试，写一大堆乱七八糟的东西",'plain','utf-8')
#发送邮箱地址
msg['From'] = from_addr
#收件箱地址
msg['To'] = to_addr
#主题
msg['Subject'] = 'the frist mail'

# server = smtplib.SMTP(smtp_server)
# server.login(from_addr,password)
# server.sendmail(from_addr,[to_addr],msg.as_string())
# server.quit()

# from_addr = raw_input('From: ')
# password = raw_input('Password: ')
# # 输入SMTP服务器地址:
# smtp_server = raw_input('SMTP server: ')
# # 输入收件人地址:
# to_addr = raw_input('To: ')

# import smtplib
server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr,password)
for i in range(5):
	server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()