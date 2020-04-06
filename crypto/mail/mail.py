# coding=utf-8
import smtplib
import time
import imaplib
import email

ORG_EMAIL = "@gmail.com"
FROM_EMAIL = "address_mail" + ORG_EMAIL
FROM_PWD = "Password"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT = "993"

try:
    mail = imaplib.IMAP4_SSL(SMTP_SERVER)
    mail.login(FROM_EMAIL, FROM_PWD)
    mail.select('inbox')

    type, data = mail.search(None, 'ALL')
    mail_ids = data[0]
    id_list = mail_ids.split()

    first_email_id = int(id_list[0])
    latest_email_id = int(id_list[-1])
    for i in range(latest_email_id, first_email_id, -1):
        type, data = mail.fetch(i, 'RFC822')
        for reponse_part in data:
            if isinstance(reponse_part, type):
                msg = email.message_from_string(reponse_part[1])
                email_subject = msg['subject']
                email_from = msg['from']

                if 'confirmation' in msg['subject']:
                    print 'Keyword a été trouver'
                    print msg['from']
except Exception, e:
    print str(e)
