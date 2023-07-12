#using fixer.io api to get rates and prices

import requests
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import url, rules, senderEmail, appPassword, receivers




def get_rates():
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.text)
    return None



def archive(filename, rates):
    with open("archive/"+filename+".json", 'w') as f:
        f.write(json.dumps(rates))



def mail_service(timestamp, rates):
    subject = "Currency rates at " + timestamp
    if rules["preferred"] is not None:
        tmp = dict()
        for currency in rules['preferred']:
            tmp[currency] = rates[currency]
        rates = tmp
    body = json.dumps(rates)
    for r in receivers:
        send_email(r, subject, body)


def send_email(toAddress, subject, body):

    message = MIMEMultipart()
    message["To"] = toAddress
    message["From"] = senderEmail
    message["Subject"] = subject
    title = "<b>"+subject+" <b>"
    message.attach(MIMEText(body))
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.ehlo("Gmail")
    server.starttls()
    server.login(senderEmail, appPassword)
    server.sendmail(senderEmail, toAddress, message.as_string())
    server.quit()


if __name__ == '__main__':
    response = get_rates()
    if rules['archive']:
        archive(str(response['timestamp']), response['rates'])
    if rules['mail']:
        mail_service(str(response['timestamp']), response['rates'])



