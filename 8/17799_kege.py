import itertools as t
comb = list(t.product('АГЕМНРТУ', repeat = 4))
k = 0
for x in comb:
    x=''.join(x)
    k+=1
    if len(x)==len(set(x)) and x[0]<x[1]<x[2]<x[3]:
        print(k, x)


