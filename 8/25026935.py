import itertools as t
s=list(t.product('ЕПСУХ', repeat=5))
k=0
sogl='ПСХ'
for x in s:
    x=''.join(x)
    if x[-1] in sogl:
        k+=1
    if x=='УСПЕХ':
        print(k)
