#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import smtplib,time
#server = smtplib.SMTP('******')  普通邮箱服务器
server = smtplib.SMTP_SSL('smtp.qq.com',465)    #QQ邮箱服务器
server.login('*******@qq.com','kz*********fbg')
for i in range(10):
  time.sleep(1)
  server.sendmail('1023625768@qq.com',['1023625768@qq.com'],
  'success!'+str(i))
server.quit()
server.close()
   
