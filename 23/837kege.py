sp=[0]*38
sp[12]=1
for i in range(13,38):
    if 12<i<20:
        sp[i]=sp[i-2]
    elif 20<i<=29:
        sp[i]=sp[i-1]
    else:
        sp[i]=sp[i-1]+sp[i-2]
print(sp[37])