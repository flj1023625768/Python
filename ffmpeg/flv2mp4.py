# -*- coding:utf-8 -*-
import os

src = os.getcwd()
f1 = r'jxout'
f =  open(f1, 'r')
f2 = f.read().split('\n')
pathss = []
for i in f2:
    path = src+i
    print(path)
    pathss.extend(path)
def zhuanma():
    for filename in pathss:
        if os.path.splitext(filename)[1]=='.flv' and os.path.splitext(filename)[0][-1]!='a' and not os.path.exists(os.path.splitext(filename)[0]+".mp4"):
            os.system('ffmpeg -i %s %s -n'  %(filename,os.path.splitext(filename)[0]+".mp4"))
        if os.path.splitext(filename)[1]=='.flv' and os.path.splitext(filename)[0][-1]=='a' and not os.path.exists(os.path.splitext(filename)[0]+".mp3"):
            os.system('ffmpeg -i %s %s -n' %(filename,os.path.splitext(filename)[0]+".mp3"))
#zhuanma()
