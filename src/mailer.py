import smtplib
import os
import string
from dotenv import load_dotenv
import datetime

class Mailer():
    def __init__(self):
        load_dotenv()

    def sendMail(self, info: list) -> None:
        user = os.getenv('GMAIL')
        to = info[0]
        name = info[1]
        subject = info[2]
        message = info[3]
        pwd = os.getenv('GMAIL_PASSWORD')
        body = self.loadTemplate(name, message)

        mail = f"Subject: {subject}\nFrom: {user}\nTo: {to}\nContent-Type: text/html\n\n{body}"

        try:
            server=smtplib.SMTP("smtp.gmail.com",587)
            server.ehlo()
            server.starttls()
            server.login(user,pwd)
            server.sendmail(user,to,mail)
            server.close()
            print("Successfully sent the mail.")
            self.log(False, f"{datetime.datetime.now()} - Email sent to {to}\n")
        except Exception as e:
            print("Failed to send the mail..", e)
            self.log(True, f"{datetime.datetime.now()} - {e}\n")

    def loadTemplate(self, name, message) -> str:
        #Inspiration from https://stackoverflow.com/questions/41354948/passing-variables-to-html-file-on-python
        context = {
            "Name": name,
            "Message": message,
        }

        #Changed to string as the {} were interfering when using .format()
        with open("./templates/template.html", "r") as file:
            template = string.Template(file.read())

        html = template.safe_substitute(context)  # Replaces placeholders safely

        return html

    def log(self, error, message) -> None:
        file = "./logs/logs.txt"

        if (error):
            file = "./logs/errors.txt"

        with open(file, "a") as f:
            f.write(message)