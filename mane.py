#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import string
import smtplib
import imaplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from platform import python_version


def send_mails():
    def generate_text():
        length = 10
        letters = string.ascii_letters + string.digits
        rand_string = ''.join(random.choice(letters) for q in range(length))
        return rand_string

    def generate_subject():
        length = 10
        letters = string.ascii_letters + string.digits
        rand_string = ''.join(random.choice(letters) for q in range(length))
        return rand_string

    for i in range(15):
        server = 'smtp.gmail.com'
        user = 'sterben.300.nikita@gmail.com'
        password = 'TrustNO1&'

        recipients = ['sterben.300.nikita@gmail.com']
        sender = 'sterben.300.nikita@gmail.com'
        send_subject = f'{generate_subject()}'
        send_text = f'{generate_text()}'

        msg = MIMEMultipart('alternative')
        msg['Subject'] = send_subject
        msg['From'] = 'Python script <' + sender + '>'
        msg['To'] = ', '.join(recipients)
        msg['Reply-To'] = sender
        msg['Return-Path'] = sender
        msg['X-Mailer'] = 'Python/' + (python_version())

        part_text = MIMEText(send_text, 'plain')

        msg.attach(part_text)

        mail = smtplib.SMTP_SSL(server)
        mail.login(user, password)
        mail.sendmail(sender, recipients, msg.as_string())
        mail.quit()


def main_send_mail():
    server = 'smtp.gmail.com'
    user = 'sterben.300.nikita@gmail.com'
    password = 'TrustNO1&'

    recipients = ['sterben.300.nikita@gmail.com']
    sender = 'sterben.300.nikita@gmail.com'
    send_subject = 'The final of test'
    send_text = (f'{final_text[0]}\n'
                 f'{final_text[1]}\n'
                 f'{final_text[2]}\n'
                 f'{final_text[3]}\n'
                 f'{final_text[4]}\n'
                 f'{final_text[5]}\n'
                 f'{final_text[6]}\n'
                 f'{final_text[7]}\n'
                 f'{final_text[8]}\n'
                 f'{final_text[9]}\n'
                 f'{final_text[10]}\n'
                 f'{final_text[11]}\n'
                 f'{final_text[14]}\n'
                 f'{final_text[13]}\n'
                 f'{final_text[14]}\n'
                 )

    msg = MIMEMultipart('alternative')
    msg['Subject'] = send_subject
    msg['From'] = 'Python script <' + sender + '>'
    msg['To'] = ', '.join(recipients)
    msg['Reply-To'] = sender
    msg['Return-Path'] = sender
    msg['X-Mailer'] = 'Python/' + (python_version())

    part_text = MIMEText(send_text, 'plain')

    msg.attach(part_text)

    mail = smtplib.SMTP_SSL(server)
    mail.login(user, password)
    mail.sendmail(sender, recipients, msg.as_string())
    mail.quit()


send_mails()


global text
mail_num = -1
mane_dict = {}
for i in range(15):
    # This block connects to mailbox
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login('sterben.300.nikita@gmail.com', 'TrustNO1&')

    mail.list()
    mail.select("inbox")

    # This block reads the last mail in mailbox

    result, data = mail.search(None, "ALL")

    ids = data[0]
    id_list = ids.split()
    latest_email_id = id_list[mail_num]

    mail_num -= 1

    result, data = mail.fetch(latest_email_id, "(RFC822)")
    raw_email = data[0][1]
    raw_email_string = raw_email.decode('utf-8')

    # This block reads and print the subject and text of last mail

    email_message = email.message_from_string(raw_email_string)
    for payload in email_message.get_payload():
        text = payload.get_payload(decode=True).decode('utf-8')

    # This block creates dict, where keys are Subject and values are Text

    mane_dict.update({email_message['Subject']: text})

# This block counts letters and numbers in value from dict

main_list = list(mane_dict.values())
values = {'letters': 0, 'numbers': 0}
score = 0
report = []
for i in range(15):
    for q in main_list[score]:
        if q.isalpha():
            values['letters'] += 1
        elif q.isdigit():
            values['numbers'] += 1
    report.append((values['letters'], values['numbers']))
    values['letters'] = 0
    values['numbers'] = 0
    score += 1

dict_keys = list(mane_dict.keys())
dict_values = list(mane_dict.values())
final_text = []
x = 0
for i in range(15):
    final_text.append(f'Received mail on theme ({dict_keys[x]}) with message: {dict_values[x]}. '
                      f'It contains {report[x][0]} letters and {report[x][1]} numbers')
    x += 1
