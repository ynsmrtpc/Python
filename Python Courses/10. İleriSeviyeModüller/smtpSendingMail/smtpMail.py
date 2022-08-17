from email.mime.nonmultipart import MIMENonMultipart
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

message = MIMEMultipart()
message["From"] = "ynsmrtpc@gmail.com"
message["To"] = "ynsmrtpc@gmail.com"
message["Subject"] = "Smtp Mail Gönderimi"
content = """

Hello World!
SMTP ile mail gönderiyorum.
Yunus Emre Topçu

"""
message_box = MIMEText(content,"plain")
message.attach(message_box)

try: 
    mail = smtplib.SMTP("smtp.gmail.com",587)
    mail.ehlo()
    mail.starttls()
    mail.login("ynsmrtpc","FeNeR1907**")
    mail.sendmail(message["From"],message["To"],message.as_string())
    print("Mail başarıyla gönderildi!")
    mail.close()
except:
    sys.stderr.write("Bir sorun oluştu\n")
    sys.stderr.flush()