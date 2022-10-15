import os, time
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import variables as VAR
import spiders.user as USR
def sendEmail2():
    msg = MIMEText("scrawling!", "html", "utf-8")
    msg['From'] = formataddr(['lico', 'thisismy163_2@163.com'])
    msg['Subject'] = 'scrawling!'  # 不能漏

    server = smtplib.SMTP_SSL('smtp.163.com')
    server.login('thisismy163_2@163.com', 'QMYENVVJELUSFXJH')
    server.sendmail('thisismy163_2@163.com', '782413632@qq.com', msg.as_string())
    server.quit()


"""
0.维持登陆状态；
1.当套餐剩余时间为3天时，开始爬取；
2.当爬到新的套餐，并且现有套餐剩余时间变为15时，停止爬取；
"""

# t = time.localtime()
# VAR._init()
VAR.set_value('remainDay', 1)
start = VAR.get_value('remainDay')
print('sdjfhieuhfie:', start)
times = 0
while 1:
    print('-------------已经开始监控--------------')

    if VAR.get_value('remainDay') <= 10:
        print("开始爬取")
        os.system("scrapy crawl user")
        # time.sleep(20)#等二十秒再执行第二个爬虫。应该不是这个原因。
        USR.set_()
        print("sfhiefnnsdfkbns:", VAR.get_value('remainDay'))  # 为什么还是0
        VAR.printDay('remainDay')
        os.system("scrapy crawl myLico")
        print("ssfsdgrhthyj:", VAR.get_value('remainDay'))
        print("等待中……")
        time.sleep(3600)

        times += 1
        if times % 12 == 0:
            sendEmail2()
    else:
        print("等待中……")
        time.sleep(3600)

        times += 1
        if times % 12 == 0:
            sendEmail2()
