import itertools as t
s=list(t.product('0123', repeat=5))
for x in s:
    x=''.join(x)
    if x[0]!='0' and

