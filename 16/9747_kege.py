sp=[0]*2025
for i in range(len(sp)):
    if i<11:
        sp[i]=i
    else:
        sp[i]=i+sp[i-1]
print(sp[2024]-sp[2021])