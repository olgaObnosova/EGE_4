sp=[0]*10_101
for i in range(10_100,0,-1):
    if i>=10_000:
        sp[i]=1
    elif i%2==0:
        sp[i]=sp[i+3]+7
    else:
        sp[i]=sp[i+1]-3
print(sp[50]-sp[57])