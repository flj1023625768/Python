# -*- coding:utf-8 -*-
import os
import datetime
src = os.getcwd()
pathss=[]
for root, dirs, files in os.walk(src):
    path = [os.path.join(root, name) for name in files]
    pathss.extend(path)
v=[]
a=[]
m4=[]
m3=[]
def count1():
    for file in pathss:
        if os.path.splitext(file)[1]=='.flv' and os.path.splitext(file)[0][-1] !='a' and file not in v:
            v.append(file)
        if os.path.splitext(file)[1]=='.flv' and os.path.splitext(file)[0][-1] =='a' and file not in a:
            a.append(file)
def count2():
    for file in pathss:
        if os.path.splitext(file)[1]=='.mp4' and file not in m4 and os.path.splitext(file)[0]+'.flv' in v:
            m4.append(file)
        if os.path.splitext(file)[1]=='.mp3' and file not in m3 and os.path.splitext(file)[0]+'.flv' in a:
            m3.append(file)
count1()
count2()
print('当前时间为：%s' %(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
print('flv文件共有 %s 个，已转MP4 %s 个，还剩 %s 个。' %(len(v),len(m4),len(v)-len(m4)))
print('_a.flv文件共有 %s 个，已转MP3 %s 个，还剩 %s 个。' %(len(a),len(m3),len(a)-len(m3)))
