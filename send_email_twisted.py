from __future__ import print_function
import email
from twisted.mail.smtp import sendmail
from twisted.internet.task import react

def main(reactor):
    a = "This is my super awesome email, sent with Twisted !22222222222222"
    msg = email.message_from_string(a) 
    d = sendmail("**********", #邮箱服务器地址
                 "**********", #发件人
                 ["**@qq.com","**@qq.com","**@qq.com"], #收件人
    '''
    FROM:*******,
    TO:"********,
    adfasdfsdfsdfdf
    .
    ''', 
port=25,
username="*********", 
password="********", 
)
    d.addBoth(print)
    return d
react(main)
