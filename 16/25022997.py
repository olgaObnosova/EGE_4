sp=[0]*2300
for n in range(2300):
    if n<2025:
        sp[n]= n**2
    if 2025<=n<2050:
        sp[n]= 2*sp[n-1]-sp[n-2]+n
    if 2050<=n<=2100:
        sp[n] =sp[n-1]+2*sp[n-2]+3*sp[n-3]
    if n>2100:
        sp[n]=2*sp[n-1]+sp[n-2]+n
print(sp[2020]+sp[2200])