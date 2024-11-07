import itertools as t
sp=list(t.product('0123456', repeat=6))
k=0
for x in sp:
    x=''.join(x)
    if x.count('3')==1 and x[0]!='0':
        x = x.replace('3','1')
        x = x.replace('5', '1')
        if '11' not in x:
            k+=1
print(k)