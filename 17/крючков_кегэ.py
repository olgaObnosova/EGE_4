with open('17-4.txt') as f:
    sp=[]
    s=0
    a=0
    for x in f:
        sp.append(int(x))
        if int(x)%11==0:
            a+=1
            s+=int(x)
sp11=s/a
k=0
maxx=0
for i in range(len(sp)-2):
    l=0
    if abs(sp[i])%100==11:
        l+=1
    if abs(sp[i+1])%100==11:
        l+=1
    if abs(sp[i+2])%100==11:
        l+=1
    if l>=1 and (sp[i]+sp[i+1]+sp[i+2])/3>sp11:
        k+=1
        maxx=max(maxx,sp[i]+sp[i+1]+sp[i+2])
print(k, maxx)