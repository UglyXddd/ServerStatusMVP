import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders
import os
import numpy as np


# Тут адресатов из файла берем
def sendEmail(smtpHost: str, smtpPort: int, mailUname: str, mailPwd: str, fromEmail: str, mailSubject: str,
              mailContentHtml: str):
    # open file with email

    file = open("mail_user.txt", "r")
    try:
        text = file.read().replace('"', '').split(";")
    except:
        text = file.read().replace('"', '')
    recepientsMailList = text
    server = smtplib.SMTP(smtpHost, smtpPort)
    # тут запуск сервака с помощью которого письмо отправляется
    server.starttls()  # Запуск серва
    server.login(mailUname, mailPwd)
    file.close()
    # print(recepientsMailList)
    # create message object
    msg = MIMEMultipart()  # объект письма(похуй)
    msg['Subject'] = mailSubject  # Тема письма
    msg['From'] = fromEmail  # от кого
    msg['To'] = ','.join(recepientsMailList)  # Кому
    # msg.attach(MIMEText(mailContentText, 'plain'))
    # msg.attach(MIMEText(mailContentHtml, 'html'))  # Тут само содержимое письма конкретно в переменной mailContentHtml
    msg.attach(MIMEText(mailContentHtml))
    # Send message object as email using smptplib
    # Заход  в аккич с помощью пароля и логина от почты
    # msgText = msg.as_string()   # Переформатирование текста письма к удобоваримому варику
    server.send_message(msg)  # Отправка письма (от кого, список кому, текст письма)
    server.quit()  # server выключаем
    # print("Email send")


if __name__ == "__main__":
    # mail server parameters
    smtpHost = "mail.example.ru"  # SMTP server гмэйла
    smtpPort = 25  # стандартный код
    mailUname = 'monit@example.ru'  # с какой почты
    mailPwd = 'ZxCvBnMaSdF1234'  # пароль приложения гугла для защиты (если чо данные от акка есть в файле mail.txt)
    fromEmail = 'monit@example.ru'  # опять от кого

    # mail body, recepients(получатели(то-есть можно несколько)), attachment files
    mailSubject = "Уведомление!"  # Тема письма
    mailContentHtml = "345345345345"  # сам текст письма
    recepientsMailList = [""]
    sendEmail(smtpHost, smtpPort, mailUname, mailPwd, fromEmail,
              mailSubject, mailContentHtml)
