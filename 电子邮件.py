import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

mail_host = 'stmp.mail.me.com'
mail_user = 'wangzeming666@icloud.com'
mail_pass = 'wpgq-qvnt-jova-fjae'

sender = 'wangzeming666@icloud.com'
receivers = ['wangzeming666@icloud.com']

content = '''Hello, world~!\r\n
Have you see this?\r\n
Come and see me, I'm waiting for you!!!'''

message = MIMEText(content, 'palin', 'utf-8')

message['From'] = formataddr(['Wangzeming666', sender])
message['To'] = formataddr(['wangzeming666', receivers[0]])
message['Subject'] = 'A Big Hello from Wangzeming!'

try:
    smtpObj = smtplib.SMTP_SSL(mail_host,587)
    smtpObj.login(mail_user,mail_host)
    smtpObj.sendmail(sender,recievers, message.as_string())
    smtpObj.quit()
    print('OK')
except smtplib.SMTPException as e:
    print('kjh')
except smtplib.SMTPServerDisconnected as e:
    print('aksjdhfkjasdh')
