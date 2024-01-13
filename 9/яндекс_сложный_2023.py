# -*- coding: utf-8 -*-
with open('9.txt', encoding='utf-8') as f:
    sp=[]
    for x in f:
      x=x.split(';')
      if ((int(x[0])%4==0 and int(x[0])%100!=0) \
          or int(x[0])%400==0) and int(x[1])==10:
          sp.append((x))
for s in sp:
    print(s)


