with open('5373.txt') as f:
    sp=[]
    min19=999999999
    for line in f:
        sp.append(int(line))
        if int(line)>0 and int(line)%19==0:
            min19=min(min19, int(line))
#print(sp)
#print(min19)
k=0
maxx=-999999
for i in range(len(sp)-1):
    if (sp[i]+sp[i+1])<min19:
        k+=1
        maxx=max(maxx,(sp[i]+sp[i+1]))
print(k)
print(maxx)
