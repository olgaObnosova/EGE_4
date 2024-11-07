import itertools as f
s=list(f.product('01234', repeat=6))
k=0
for x in s:
    x=''.join(x)
    if x[0]=='3' and int(x,5)%2==0:
        k += 1
print(k)
print(bin(201), bin(44), bin(240), bin(33), bin(107))