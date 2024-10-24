with open('pr') as f:
    f=f.readline()
sogl='BCDF'
gl='AEU'
k=0
ind=0
print(f)
maxx=0
while ind<len(f)-2:
    print(f[ind], f[ind+1], f[ind+2])
    if f[ind] in sogl and f[ind+1] in gl and f[ind+2] in sogl:
        k+=1
        maxx=max(maxx, k)
        ind=ind+3
    else:
        k = 0
        ind=ind+1
print(maxx)
