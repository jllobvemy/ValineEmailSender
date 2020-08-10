import smtplib
import time
from email.mime.text import MIMEText
from email.header import Header

def email_sender(title: str, message: str):
    mail_host = 'smtp.163.com'
    mail_user = 'jllobvemy@163.com'
    mail_passwd = 'xxxxxxxxxxxxxxx' # 授权码

    sender = 'jllobvemy@163.com' # 发送者
    recevier = 'xxxxxxxx@qq.com' # 接受者

    message = MIMEText(message, 'plain', 'utf-8') # 邮件信息
    message['From'] = 'jllobvemy@163.com'
    message['To'] = 'xxxxxxxxx@qq.com'

    message['Subject'] = Header(title, 'utf-8')
    ctime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) # 获取当前时间
    f = open('sendinglog.txt', 'a+')
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)
        smtpObj.login(mail_user, mail_passwd) # 登录
        smtpObj.sendmail(sender, recevier, message.as_string()) # 发送邮件
        print('sending succeed')
        f.write(ctime + ': ' + 'sending succeed' + '\n') #更新日志
    except smtplib.SMTPException as e:
        f.write(ctime + ': error: ' + str(e).strip('(').strip(')') + '\n') # 更新日志
        print('error: ', str(e))

    f.close()

if __name__ == '__main__':
    email_sender('test title3', 'test message3')
