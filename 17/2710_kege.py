with open('17_2710.txt') as f:
    sp=[]
    maxx=0
    for x in f:
        sp.append(int(x))
k=0

for i in range(0, len(sp)):
    if i==0:
        if sp[i]<sp[i+1]:
            k+=1
    elif i==len(sp)-1:
        if sp[i]<sp[i-1]:
            k+=1
    else:
        if sp[i]<sp[i-1] and sp[i]<sp[i+1]:
            k+=1
            maxx=max(maxx, sp[i-1]-sp[i])
            maxx=max(maxx, sp[i+1]-sp[i])
print(k, maxx)