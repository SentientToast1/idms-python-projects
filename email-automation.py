from email.message import EmailMessage
import ssl
import smtplib


fromMail = ''
appPassword = ''
toMail = ''




subject = 'Top 5 news of today'


with open("top 5 news.txt",'r') as file:
    body = file.read()

em = EmailMessage()
em['From'] = fromMail
em['To'] = toMail
em['Subject'] = subject
em.set_content(body)


context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(fromMail,appPassword)
    smtp.sendmail(fromMail,toMail, em.as_string()) 