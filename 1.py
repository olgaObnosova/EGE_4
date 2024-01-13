sp=[]
maxx=0
maxs=0
k=0
with open('17.txt') as f:
    for line in f:
        sp.append(int(line))
        if int(line)%100==15:
            maxx=max(maxx, int(line))
for i in range(len(sp)-2):
    if ((len(str(sp[i]))==4  and len(str(sp[i+1]))!=4 \
            and len(str(sp[i+2]))!=4) or \
            (len(str(sp[i+1])) == 4 and len(str(sp[i])) != 4 \
             and len(str(sp[i + 2])) != 4) or \
            (len(str(sp[i+2])) == 4 and len(str(sp[i])) != 4 \
             and len(str(sp[i+1])) != 4)) and \
            (sp[i]+sp[i+1]+sp[i+2])>=maxx:
        k+=1
        maxs=max(maxs,(sp[i]+sp[i+1]+sp[i+2]))
print(k, maxs)






