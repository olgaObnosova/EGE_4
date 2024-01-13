sp=[0]*70
for i in range(len(sp)):
    if i<3:
        sp[i]=i
    if i>2:
        sp[i]=(2*i-1)*(sp[i-1]+sp[i-2])
print(sp[69]%10**9)