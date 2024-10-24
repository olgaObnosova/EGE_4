import fnmatch as f
for i in range(10**12,0, -1):
    if i%98==0 and i%392!=0:
        print(i)
        break
k=0
for i in range(999999999838, 980793114, -98):
    if f.fnmatch(str(i), '98?7*93?24') and i%392!=0:
        k+=1
        print(i, i//98)
        if k==7:
            break