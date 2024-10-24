sp=[0]*2030
for i in range(1, 2030):
    if i==1:
        sp[i]=1
    else:
        sp[i]=i*sp[i-1]
print((2*sp[2024]+sp[2023])//sp[2022])