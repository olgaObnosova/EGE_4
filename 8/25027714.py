import itertools as t
#l1=list(t.permutations('123', r=3))
l2=list(t.product('012345678', repeat=6))
k=0
for x in l2:
    x=''.join(x)
    if int(x)%2==0 and x[0]!='0' and\
        x.count('0')+x.count('2')+x.count('4')+ \
            x.count('6')+x.count('8')<=2:
        k+=1
print(k)