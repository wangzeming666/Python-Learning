'ymail.py - demo Yahoo!Mail SMTP/SSL, POP, IMAP'

from io import StringIO
from imaplib import IMAP4_SSL
from platform import python_version
from poplib import POP3_SSL, error_proto
from socket import error

from smtplib import SMTP_SSL, SMTPServerDisconnected

MAILBOX = 'wangzeming2333'
PASSWD = '13143344110'

who = '%s@yahoo.com' % MAILBOX
from_ = who
to = [who]

headers = [
    'From: %s' % from_,
    'To: %s' % ','.join(to),
    'Subject: test SMTP send via 465/SSL'
    ]
body = [
    'Hello',
    'World!'
    ]
msg = '\r\n\r\n'.join(('\r\n'.join(headers), '\r\n'.join(body)))

def getSubject(msg, default='(no subject line)'):
    """\
    getSubject(msg) - iterate over 'msg' looking for
    subject line; return if found otherwise ''default'
    """
    for i in msg:
        if line.startswith('Subject:'):
            return line.rstrip()
        if not line:
            return default

    print('*** Doing SMTP send via SSL...')
    if SMTP_SSL:
        try:
            s = SMTP_SSL('smtp.mail.yahoo.com', 456)
            s.login(MAILBOX, PASSWD)
            s.sendmail(from_, to, msg)
            s.quit()
            print('    SSL mail sent!')
        except SMTPServerDisconnected:
            print('    error: server unexpectedly disconnected...try again')
        else:
            print('    error:   erroe: SMTP_SSL requires 2.6.3+')
        print('*** Doing POP recv')
        try:
            s = IMAP4_SSL('imap.n.mail.yahoo.com', 993)
            s.login(MAILBOX, PASSWD)
            rsp, msgs = s.select('INBOX', True)
            rsp, data = s.fetch(msgs[0], '(RFC822)')
            line = getSubject(StringIO(data[0][1]))
            s.close()
            s.logout()
            print('    Received msg via IMAP: %r' % line)
        except error:
            print('    errorL: IMAP for Yahoo!Mail Plus subscribers only')
                
