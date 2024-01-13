with open('17.txt') as f:
    sp=[]
    maxx=0
    for x  in f:
        sp.append(int(x))
        if int(x)%100==19:
            maxx=max(maxx, int(x))
k=0
maxs=0
for i in range(len(sp)-1):
    if ((len(str(sp[i]))==4 and len(str(sp[i+1]))==4 and len(str(sp[i+2]))!=4) or \
       (len(str(sp[i]))==4 and len(str(sp[i+1]))!=4 and len(str(sp[i+2]))==4) or \
       (len(str(sp[i]))!=4 and len(str(sp[i+1]))==4 and len(str(sp[i+2]))==4)) and \
       (len(str(sp[i]))%3==0 or \
        len(str(sp[i+1]))%3==0 or len(str(sp[i+2]))%3==0) and \
       (sp[i]+sp[i+1]+sp[i+2])>maxx:
        k+=1
        maxs=max(maxs, sp[i]+sp[i+1]+sp[i+2])
print(k, maxs)
print(maxx)