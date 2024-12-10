import itertools as t
comb=list(t.product('12', repeat=12))
s=set()
for x in comb:
    nac=3
    for y in x:
        if y=='1':
            nac=nac+1
        if y=='2':
            nac=nac*2-3
    s.add(nac)
print(len(s))
