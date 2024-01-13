with open('17_7267.txt') as f:
    minn=999999999
    sp=[]
    for line in f:
        sp.append(int(line))
        if int(line)<minn:
            minn=int(line)
k=maxx=0
for i in range(len(sp)-1):
    if sp[i]%117==minn or sp[i+1]%117==minn:
        k+=1
        maxx=max(maxx, sp[i]+sp[i+1])
print(k)
print(maxx)