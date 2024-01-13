with open('25019141.txt') as f:
    sp = [int(x) for x in f]
minn = float('inf')
min2 = float('inf')
k=0
for i in range(len(sp)-1):
    if (abs(sp[i])%10==3 \
            and abs(sp[i+1])%10!=3) or \
            (abs(sp[i+1]) % 10 == 3 \
             and abs(sp[i - 1]) % 10 != 3):
        minn= min(minn,sp[i],sp[i+1])
r=9**2+9**2+8**2+3**2
for i in range(len(sp)):
    if '3' in str(sp[i])  and sp[i]>=r:
        k+=1
        min2=min(min2, sp[i])

print(k)
print(min2)