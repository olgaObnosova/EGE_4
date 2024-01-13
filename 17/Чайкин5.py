with open('17.чайкин5.txt') as f:
    sp=[]
    maxx=0
    for x  in f:
        sp.append(int(x))
k=0
minn=99999999
for i in range(len(sp)-1):
    if ((len(str(sp[i]))==4 and len(str(sp[i+1]))==4 and len(str(sp[i+2]))!=4) or \
       (len(str(sp[i]))==4 and len(str(sp[i+1]))!=4 and len(str(sp[i+2]))==4) or \
       (len(str(sp[i]))!=4 and len(str(sp[i+1]))==4 and len(str(sp[i+2]))==4)):
        s = sp[i]+sp[i+1]+sp[i+2]
        if s>0 and int(s**0.5) == s**0.5:
            k+=1
            minn=min(minn, sp[i]+sp[i+1]+sp[i+2])
print(k, minn)