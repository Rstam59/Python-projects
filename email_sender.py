import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
html = Template(Path("index.html").read_text())
email = EmailMessage()
email['from'] = 'rustem aliyev'
email['to'] = 'rustem.alivey.1999@gmail.com'
email['subject'] = "This message comes from you!"

email.set_content('i just wanna test my program or you who knows')
with smtplib.SMTP(host= 'smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('rustem.alivey.1999@gmail.com','elonmusk345')
    smtp.send_message(email)
    print("sent")

