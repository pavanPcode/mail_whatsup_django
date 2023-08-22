import smtplib
def mail_send(gmail,text):

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    # start TLS for security
    s.starttls()
    # Authentication
    s.login('rangusaipavan6@gmail.com', 'iqmzphegahahetxe')

    # message to be sent
    # sending the mail
    message = f"""From: From Person <rangusaipavan6@gmail.com>
    To: To Person <{gmail}>
    Subject: SMTP e-mail test

    {text}
    """


    data = s.sendmail('rangusaipavan6@gmail.com', gmail, message)

    # terminating the session
    s.quit()
    return {"status":"success"}



def send_whatsApp_message(mobile,message):
    import requests


    x = requests.get(f'https://bookmyotservice.pythonanywhere.com/sendWhatsAppMessage?number={mobile}&message={message}')

    return  str(x.text)