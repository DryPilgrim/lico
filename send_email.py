import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


def sendEmail():
    msg = MIMEText("dry There be the best package!", "html", "utf-8")
    msg['From'] = formataddr(['lico', 'thisismy163_2@163.com'])
    msg['Subject'] = 'lico be dry'  # 不能漏

    server = smtplib.SMTP_SSL('smtp.163.com')
    server.login('thisismy163_2@163.com', 'QMYENVVJELUSFXJH')
    server.sendmail('thisismy163_2@163.com', '782413632@qq.com', msg.as_string())
    server.quit()


def sendEmail2():
    msg = MIMEText("scrawling!", "html", "utf-8")
    msg['From'] = formataddr(['lico', 'thisismy163_2@163.com'])
    msg['Subject'] = 'scrawling!'  # 不能漏

    server = smtplib.SMTP_SSL('smtp.163.com')
    server.login('thisismy163_2@163.com', 'QMYENVVJELUSFXJH')
    server.sendmail('thisismy163_2@163.com', '782413632@qq.com', msg.as_string())
    server.quit()
