with open('17.txt') as f:
    sp = []
    minn=999999999999999
    for x in f:
        sp.append(int(x))
        if int(x)%10==5 and 99<x<1000:
            minn=min(minn, int(x))
k=0
minnn=9999999999
for i in range(len(sp)-1):
    if ((len(str(abs(sp[i])))!=3 and len(str(abs(sp[i+1])))==3) or \
            (len(str(abs(sp[i])))==3 and len(str(abs(sp[i+1])))!=3)) and \
           (sp[i]+sp[i+1])%minn==0:
            k+=1
            minnn=min(minnn, sp[i]+sp[i+1])
print(k, minnn)