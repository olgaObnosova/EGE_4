sp=[0]*10_004
for i in range(10_003,-1,-1):
    if i>=10000:
        sp[i]=1
    elif i<10000 and i%2==0:
        sp[i]=sp[i+3]+7
    else:
        sp[i]=sp[i+1]-3
print(sp[50]-sp[57])