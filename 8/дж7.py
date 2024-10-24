import itertools as t
sp=list(t.permutations('ннгипе',r=6))
print(len(sp))
s=set()
for x in sp:
    x=''.join(x)
    s.add(x)
print(len(s))

