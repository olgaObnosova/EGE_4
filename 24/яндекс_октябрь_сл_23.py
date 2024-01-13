with open ('24yan.txt') as f:
    f=f.readline()
k=0
f=f.split('E')
minn=9999999
print(f[:3])
for i in range(len(f)-99):
    s=0
    for j in range(i, i+99):
        s+=len(f[j])
    minn=min(minn, s)
print(minn+100)