#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import string
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from platform import python_version


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


for i in range(10):
    server = 'smtp.gmail.com'
    user = 'gavrilov.3.nikita@gmail.com'
    password = 'WARface2002'

    recipients = ['sterben.300.list@gmail.com', 'gavrilov.3.nikita@gmail.com']
    sender = 'gavrilov.3.nikita@gmail.com'
    subject = f'{generate_subject()}'
    text = f'{generate_text()}'
    html = '<html><head></head><body><p>' + text + '</p></body></html>'

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = 'Python script <' + sender + '>'
    msg['To'] = ', '.join(recipients)
    msg['Reply-To'] = sender
    msg['Return-Path'] = sender
    msg['X-Mailer'] = 'Python/' + (python_version())

    part_text = MIMEText(text, 'plain')
    part_html = MIMEText(html, 'html')

    msg.attach(part_text)
    msg.attach(part_html)

    mail = smtplib.SMTP_SSL(server)
    mail.login(user, password)
    mail.sendmail(sender, recipients, msg.as_string())
    mail.quit()
