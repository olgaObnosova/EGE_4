import itertools as t

s = list(t.product('0123', repeat=5))
d = list(t.permutations('01234567', r=5))
k = 0
for x in d:
    x = ''.join(x)
    f = 1
    for i in range(len(x) - 1):
        if int(x[i]) % 2 == int(x[i + 1]) % 2:
            f = 0
    if f and '1' not in x and x[0] != '0':
        k += 1

print(k)
