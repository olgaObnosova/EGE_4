with open ('24-yand_1.txt') as f:
    f=f.readline()
    f=f.replace('AB', '*')
k=1
maxx=0
for i in range(len(f)): # ABCDFAB *CDF*
    if f[i]!='*':
        k+=1
        maxx=max(maxx, k)
    else:
        k+=1
        maxx = max(maxx, k)
        k=1
print(maxx)