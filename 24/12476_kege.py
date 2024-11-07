with open('24_12476.txt') as f:
    f = f.readline()
    f = f.replace('ORO', '@')
    f = f.replace('ROR', '@')
    f = f.replace('RO', '*')
    f = f.split('*')

print(f[:3])
maxx = 0
for i in range(0, len(f) - 21):
    s = 'RO'.join(f[i:i + 22])
    s = s.split('@')
    for x in s:
        if len(x)>maxx:
            maxx=max(maxx, len(x))
            otv=x
    # a = len(s)
    # if '@' not in s:
    #     maxx = max(maxx, a)
    #     otv = s
print(maxx)
print(otv)