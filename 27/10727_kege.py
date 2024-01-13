with open('27-A_10727.txt') as f:
    n=int(f.readline())
    sp=[int(x) for x in f]
otv=0
for i in range(n):
    for j in range(i, n):
        kp=ko=0
        for k in range(i, j+1):
            if sp[k]>0:
                kp+=1
            if sp[k]<0:
                ko+=1
        if kp==ko:
            otv+=1
print(otv)