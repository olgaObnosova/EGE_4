def dv(n):
    s=''
    while n>0:
        ost = n % 13
        if ost ==10:
            s+='a'
        elif ost == 11:
            s+='b'
        else:
            s+=str(ost)
        n=n//13
    return s[::-1]

with open('17_9872.txt') as f:
    sp=[]
    maxx=-10**10
    for x in f:
        x=int(x)
        sp.append(x)
        if dv(abs(x))[-2:]=='12':
            maxx=max(maxx, x)
pr=0
cnt=0
for i in range(len(sp)-2):
    k=0
    if len(str(abs(sp[i])))==3:
        k+=1
    if len(str(abs(sp[i+1]))) == 3:
        k += 1
    if len(str(abs(sp[i+2]))) == 3:
        k += 1
    if k==2 and sp[i]+sp[i+1]+sp[i+2]< maxx:
        cnt+=1
        pr=max(pr, sp[i]*sp[i+1]*sp[i+2])
print(cnt, pr)

