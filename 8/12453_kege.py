import itertools as f
s = set(f.permutations('СОВЕСТЬ', r=7))
k = 0
for x in s:
    x = ''.join(x)
    x = x.replace('О', '*')
    x = x.replace('Е', '*')
    x = x.replace('Ь', '*')
    x = x.replace('С', '@')
    x = x.replace('В', '@')
    x = x.replace('Т', '@')
    if not ('**' in x and '@@' in x):
        k += 1
print(k)