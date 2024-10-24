sp=[0]*2030
for i in range(1, 2030):
    if i<7:
        sp[i]=7
    else:
        sp[i]=i+1+sp[i-2]
print(sp[2024]-sp[2020])
