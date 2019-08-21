# -*- coding:utf-8 -*-
import os
#创建目录函数
src = os.getcwd()
pathss=[]
for root, dirs, files in os.walk(src):
    path = [os.path.join(root, name) for name in files]
    pathss.extend(path)
f = open('outv.txt','a')
f1 = open('outvz.txt','a')


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
        if os.path.splitext(file)[1]=='.mp4' and file not in m4 and os.path.splitext(file)[0]+'.flv' in v:
            m4.append(file)
        if os.path.splitext(file)[1]=='.mp3' and file not in m3 and os.path.splitext(file)[0]+'.flv' in a:
            m3.append(file)
count1()

file='/data/www/www/flv/streams/pri/zk/zkjj/J_00087_1504/J1504_00087_ch1301.mp4'
if os.path.splitext(file)[1]=='.mp4' and file not in m4 and os.path.splitext(file)[0]+'.flv' in v:
    print 1
if file in pathss:
    print 2
print  os.path.splitext(file)[0]
# for i in v:
#
#     f.write(i+'\n')
# f.close()
