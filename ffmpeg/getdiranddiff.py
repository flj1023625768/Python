#! -*- coding:utf-8 -*-
import os

f1 = r'flv.txt'
f1 =  open(f1, 'r')
f1 = f1.read().split('\n')
f2 = r'nas.txt'
f2 =  open(f2, 'r')
f2 = f2.read().split('\n')
f3 = r'in'
f4 = r'out'

f6 = open(f3,'a')
f7 = open(f4,'a')

n1 = 0
n2 = 0

for i in f2:
  if i in f1:
    n1 += 1
    f6.write(i+'\n')
  else:
    n2 += 1
    f7.write(i+'\n')

f6.write(str(n1)+'\n')
f7.write(str(n2)+'\n')
