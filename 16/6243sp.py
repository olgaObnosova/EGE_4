sp=[0]*2024
for i in range(2024):
    if i<=2:
        sp[i]=i
    else:
        sp[i]=i+sp[i-2]
print(sp[2023]+sp[2020])