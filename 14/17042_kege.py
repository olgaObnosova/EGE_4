a=17*1331**166-5*121**20-3*11**77+1334
k=s=0
while a!=0:
    s+= a%11

    a=a//11
print(s)
print(k)