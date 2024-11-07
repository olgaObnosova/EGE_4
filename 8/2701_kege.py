import itertools as t
sp1=list(t.product('АВЕЛРФЬ',repeat=6))
k=0
for x in sp1:
    x=''.join(x)
    k+=1
    if x.count('А')+x.count('Е')==0:
        print(k)
        break