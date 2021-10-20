import smtplib
from email.mime.text import MIMEText


def send_email(email, height, average_height):

    from_email = "ysanthanam87@gmail.com"
    from_password = "988434@Yas"
    to_email = email

    subject = "Height data"
    message = "Hey there, your height is %s. Average height of all is %s" % (height, average_height)

    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)


