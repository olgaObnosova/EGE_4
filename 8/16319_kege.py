import itertools as t
comb = list(t.product('АПРСУ', repeat = 5))
k=0
for x in comb:
    x=''.join(x)
    k+=1
    if x.count('У')<=1 and 'АА' not in x:
        print(k, x)