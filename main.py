import smtplib

def sendmailalternative(sender, password, receiver, title, message):
    try:
        msg = EmailMessage()
        msg.set_content(message)

        msg['Subject'] = title
        msg['From'] = sender
        msg['To'] = receiver

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        sleep(3)
        server.login(sender, password)
        sleep(3)
        server.send_message(msg)
        server.quit()
        return "Email sent"
    except Exception as err:
        return err
