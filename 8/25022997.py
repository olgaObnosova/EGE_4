import itertools as t
sl=list(t.product('ЛМСЫЬ',repeat=5))
for i in range(len(sl)):
    x=''.join(sl[i])
    if x[0]=='Ы' and x[1]=='Ы':
        print(sl[i], i+1)
print(int('33443',5))