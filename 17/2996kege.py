with open('17_2996.txt') as f:
    k=0
    sp=[]
    for line in f:
        sp.append(int(line))
        if abs(int(line))<100:
            k+=1
count=0
maxx=0
for i in range(len(sp)-1):
    sr=(sp[i]+sp[i+1])/2
    if sr>k:
        count+=1
        maxx=max(maxx, sp[i]+sp[i+1])
print(count, maxx)
