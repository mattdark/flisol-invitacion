#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import smtplib
import os
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
from email_login import fromaddr, password
import xlrd

workbook = xlrd.open_workbook('./speakers/speakers.xls')
worksheet = workbook.sheet_by_name('Speakers')
for x in range(1,5,1):
    id = str(int(worksheet.cell(x,0).value))
    filename = id + '.pdf'
    toaddr = worksheet.cell(x,5).value
    cc = worksheet.cell(x,6).value

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Cc'] = cc
    msg['Subject'] = "Invitación FLISoL Tapachula"

    body = """\
    <html>
      <head></head>
      <body>"""

    with open('message', 'r') as mymessage:
        body += mymessage.read().replace('\n', '')

    body += """</body>
    </html>
    """

    msg.attach(MIMEText(body, 'html'))

    attachment = open("./speakers/" + filename, "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, password)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
