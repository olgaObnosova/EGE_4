with open('17_8373.txt') as f:
    sp=[]
    minn=999999999
    for line in f:
        sp.append(int(line))
        if int(line)%2==0:
            minn=min(minn, int(line))
k=0
mins=9999999
for i in range(len(sp)-2):
    if sp[i]%2!=sp[i+2]%2 and sp[i+1]%minn==0:
        k+=1
        mins=min(mins, sp[i]+sp[i+2])
print(k, mins)


