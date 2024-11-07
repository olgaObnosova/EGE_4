import itertools as t
s=list(t.permutations('01234567', r=6))
k=0
for x in s:
    x=''.join(x)
    if x[0]!='0'  and int(x,8)%5==0:
        if int(x[0])%2!=int(x[1])%2 and int(x[1])%2!=int(x[2])%2\
            and int(x[2])%2!=int(x[3])%2 and int(x[3])%2!=int(x[4])%2 \
                and int(x[4]) % 2 != int(x[5]) % 2:
            k+=1
print(k)