sp=[0]*36
for i in range(len(sp)):
    if i<3:
        sp[i]=i
    elif i>2 and i%2==0:
        sp[i]=3*(i-1)+sp[i-1]+5
    else:
        sp[i] = 3 * (i + 1) + sp[i - 2] -2
print(sp)