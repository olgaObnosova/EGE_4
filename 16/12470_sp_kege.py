sp=[0]*40
for i in range(1, 40):
    if i<3:
        sp[i]=i
    if i>2 and i%2!=0:
        sp[i]=sp[i-1]+sp[i-2]+1
    if i > 2 and i % 2 == 0:
        sp[i]=sum(sp[1:i])
print(sp[38])