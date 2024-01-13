sp=[0]*1001
sp[1]=1
for i in range(2,1001):
    if i%3==0:
        sp[i]=i*sp[i//3]-1
    else:
        sp[i]=i
print(sp[1000]/sp[997])