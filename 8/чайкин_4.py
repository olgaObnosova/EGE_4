import itertools as t
l = list(t.product('0123456789AB', repeat=8))
k = 0
for x in l:
    x = ''.join(x)
    if int(x[0],12)%2!=int(x[-1],12) and\
        x.count('2')+x.count('3')+x.count('5')+\
x.count('7')+x.count('B')>=2 and x[0]!='0':
        k+=1
print(k)
