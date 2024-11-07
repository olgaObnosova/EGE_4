with open('24.14_14647.txt') as f:
    k=0
    f=f.readline()
    sp=[]
    for x in f:
        if x=='X' or x=='Y':
            sp.append(k)
            sp.append(x)
            k=0
        else:
            k+=1
maxx=0
'''
for x in sp:
    if x!='X' and x!='Y':
        maxx=max(maxx, x)
t= sp.index(maxx)
print(sp[t-5: t+5])
'''
summ=0
for i in range(len(sp)):
    r=sp[i:i+5]
    while 'X' in r:
        r.remove('X')
    while 'Y' in r:
        r.remove('Y')
    if len(r)>0:
        summ=sum(r)
    if summ>maxx:
        maxx=summ
        otv=i
print(maxx, otv)
print(sp[otv-5: otv+5])
