sp=[0]*10010
for i in range(10009,0,-1):
    if i>=10000:
        sp[i]=i
    elif i<10_000 and i%2==0:
        sp[i]=sp[i+2]-3
    elif i<10_000 and i%2!=0:
        sp[i]=sp[i+2]+1
print(sp[94]-sp[80])
