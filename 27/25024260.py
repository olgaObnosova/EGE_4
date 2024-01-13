sp=[0]*1402
for i in range(1402):
    if i<4:
        sp[i]=1
    if i>3:
        sp[i]=sp[i-1]*(i-3)
print(sp[1401]/sp[1397])