with open('26_4336.txt') as f:
    n=int(f.readline())
    sp=[]
    for x in f:
        a, b =map(int, x.split())
        sp.append([a,b])
#sp.sort()
vr=['0']*86400
for x in sp:
    a, b=x
    for j in range(a, b+1):
        vr[j]='1'
vr=''.join(vr)
print(vr.count('0'))
print(vr.count('10'))