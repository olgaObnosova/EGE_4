with open('27_B_9475.txt') as f:
    n=int(f.readline())
    sp=[int(x) for x in f]
print((sum(sp)-87-1697)%23)
spo=[10**9]*23
sp3=[]
for x in sp:
    if x%23==18:
        sp3.append(x)
    spo[x%23]=min(spo[x%23], x)
print(spo)
sp3.sort()
print(sp3[:5])
print(n-2)




