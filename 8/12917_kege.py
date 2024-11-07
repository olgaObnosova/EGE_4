import itertools as f
s = list(f.permutations('ООПРСТ', r=6))

k = set()
for x in s:
    x = ''.join(x)
    if 'ОО' not in x:
        k.add(x)
print(len(k))