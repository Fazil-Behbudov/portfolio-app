import smtplib,ssl

def send_mail(message):
    host = "smtp.gmail.com"
    port = 465
    user = "behbudovfazil11@gmail.com"
    password = "ogog cdbu xeyw kzin"
    receiver = "behbudovfazil11@gmail.com"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(user, password)
        server.sendmail(user, receiver, message)


