sp=[0]*64
sp[3]=1
for i in range(4,28):
    if i%2==0:
        sp[i]=sp[i//2]+sp[i-3]
    else:
        sp[i]=sp[i-3]
for i in range(30, 54):
    sp[i]=sp[i-3]
for i in range(54, 64):
    if i%2==0:
        sp[i]=sp[i//2]+sp[i-3]
    else:
        sp[i]=sp[i-3]
print(sp[63])