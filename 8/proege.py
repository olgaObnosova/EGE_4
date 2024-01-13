import itertools as t

k = 0
#st = list(t.permutations('ЭФЕКТ', r=5))
st2 = list(t.product('01234567', repeat=5))
print(st2[:10])
for x in st2:
    x=''.join(x)
    if x[0]!='0' and x.count('6')==1 and '16' not in x \
                            and '61' not in x and '36' not in x \
                            and '63' not in x and '56' not in x and \
                            '65' not in x and '76' not in x and \
                            '67' not in x:
        k+=1
print(k)