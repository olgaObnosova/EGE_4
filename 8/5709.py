import itertools as t

k = 0
st = list(t.permutations('ЭФЕКТ', r=5))
st2 = list(t.product('ЭФЕКТ', repeat=5))
print(st[1])
print(st2[1])
for x in st:
    x = ''.join(x)
    if x.index('Е') < x.index('Э') \
            and x.index('Ф') < x.index('Т') \
            < x.index('К'):
        k += 1
print(k)
