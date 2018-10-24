

from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText


def main():
    sender = '24488954@qq.com'
    receive = ['187717@163.com']
    message = MIMEText('hello python some test code', 'plain', 'utf-8')
    message['From'] = Header('tome', 'utf-8')
    message['To'] = Header('骆昊', 'utf-8')
    message['Subject'] = Header('示例代码实验邮件', 'utf-8')

    smtper = SMTP('smtp.126.com')
    smtper.login(sender, '****')
    smtper.sendmail(sender, receive, message.as_string())
    print('邮件发送完成!')


main()
