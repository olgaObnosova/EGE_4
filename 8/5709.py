from itertools import permutations

k = 0
st = list(permutations('ЭФЕКТ', r=5))
print(st[0])
for x in st:
    x = ''.join(x)
    if x.index('Е') < x.index('Э') and x.index('Ф') < x.index('Т') < x.index('К'):
        k += 1
print(k)
