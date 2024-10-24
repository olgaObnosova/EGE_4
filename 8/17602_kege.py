import itertools as t
comb= list(t.product('0123456789abcd', repeat=5))
k=0
for x in comb:
    x=''.join(x)
    if x[0]!='0' and x.count('9')==1 \
            and x.count('b')+x.count('c')+x.count('d')<=3:
        k+=1
print(k)