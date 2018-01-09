#!/usr/bin/env python
# -*- coding: UTF-8 -*-
class Complex:
  def __init__(self, rel, img):
    self.rel = rel
    self.img = img
  def add(self, c):
    self.rel += c.rel
    self.img += c.img
  def sub(self, c):
    self.rel -= c.rel
    self.img -= c.img
  def mul(self, c):
    r = self.rel * c.rel -self.img * c.img
    i = self.img * c.rel + self.rel * c.img
    self.rel = r
    self.img = i
  def div(self, c):
    t = c.rel * c.rel + c.img * c.img
    r = self.rel*c.rel + self.img*c.img
    i = self.img*c.rel - self.rel*c.img
    t = 1.0 * t
    self.rel = r / t
    self.img = i / t
  def out(self):
    if self.img < 0:
      x="("+str(self.rel)+str(self.img)+"j"+")"
    else:
      x="("+str(self.rel)+"+"+str(self.img)+"j"+")"
    return x
#txt='(1+2j)+((3+4j )+        (5+6j))*(3+4j)+(3+3j)'
txt='(1+3j)+(5-7j)-(((8-8j)+(7-8j)*(6+5j))/(9+8j))+((8-2j)-(2+5j)/(1-3j))'
#txt='(4+7j)-(8-9j)/(3-2j)'
#txt='(1+3j)+(5-7j)-(4.4-6.2j)'
#txt=txt.replace(" ","")
#txt=raw_input()
#txt=txt.replace(" ","")
print '%s = ' %(txt)
newtxt='a1+(a2-a3)*a4+a5'
def toList(txt):
  n=0
  a=[]
  k=0
  j=0
  l=len(txt)
  for i in range(l):
    
    if  txt[i] == '(':
      if i - k == 2:
        a.append(txt[k+1])
      n += 1
      if n == 2:
         a.append(txt[i-1])
         n -= 1
      j = i
    elif txt[i] == ')':
      n -= 1
      k = i
      if n == 0:
         a.append(txt[j:k+1])
      else:
         a.append(txt[i])
         n += 1
  return a
def getCom(i):
  x=Complex(0,0)
  l=len(i)
  if "+" in i:
    index=i.index("+")
    x.rel=float(i[1:index])
    x.img=float(i[index+1:l-2]) 
  elif "-" in i:
    index=i.index("-")
    x.rel=float(i[1:index])
    x.img=-float(i[index+1:l-2]) 
  return x
def toCal(a):
  while "*" in a:
    i = a.index("*")
    x=getCom(a[i-1])
    y=getCom(a[i+1])
    a1=Complex(x.rel,x.img)
    a2=Complex(y.rel,y.img)
    a1.mul(a2)
    a[i+1]=a1.out()
    a.pop(i-1)
    a.pop(i-1)
    toCal(a)
  while "/" in a:
    i = a.index("/")
    x=getCom(a[i-1])
    y=getCom(a[i+1])
    a1=Complex(x.rel,x.img)
    a2=Complex(y.rel,y.img)
    a1.div(a2)
    a[i+1]=a1.out()
    a.pop(i-1)
    a.pop(i-1)
    toCal(a)
  while "-" in a:
    i = a.index("-")
    x=getCom(a[i-1])
    y=getCom(a[i+1])
    a1=Complex(x.rel,x.img)
    a2=Complex(y.rel,y.img)
    a1.sub(a2)
    a[i+1]=a1.out()
    a.pop(i-1)
    a.pop(i-1)
    toCal(a)
  while "+" in a:
    i = a.index("+")
    x=getCom(a[i-1])
    y=getCom(a[i+1])
    a1=Complex(x.rel,x.img)
    a2=Complex(y.rel,y.img)
    a1.add(a2)
    a[i+1]=a1.out()
    a.pop(i-1)
    a.pop(i-1)
    toCal(a)
  return a
def toTry(li):
  while not "(" in li:
    return toCal(li)
  n=0
  j=0
  k=0
  for i in range(len(li)):
    if li[i] == "(":
      n += 1
      if n == 1:
        j = i
    elif li[i] == ")":
      n -= 1
      if n == 0:
        k = i
  newli=li[j+1:k]
  nli=toTry(newli)
  qli=li[0:j]
  hli=li[k+1:]
  qli.extend(nli)
  qli.extend(hli)
  print qli
  n=toTry(qli)
  return n
a=toList(txt)
b=toTry(a)
print b[0]

