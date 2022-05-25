# Python code to illustrate Sending mail with attachments
# from your Gmail account

# libraries to be imported
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = "pawarbt2009@gmail.com"
toaddr = "devloperp9@gmail.com"

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = input("please insert the subject: ")
body = "Body_of_the_mail"
msg.attach(MIMEText(body, 'plain'))
filename = input("Please enter Exact file name from above list: ")
attachment = open(f"C:/Users/Pratik/Downloads/{filename}", "rb")
p = MIMEBase('application', 'octet-stream')
p.set_payload((attachment).read())
encoders.encode_base64(p)
p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msg.attach(p)
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(fromaddr, "Pratik@123")
text = msg.as_string()
s.sendmail(fromaddr, toaddr, text)
s.quit()
