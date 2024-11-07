import itertools as t
sp=list(t.product('012345678', repeat=6))
print(sp[:10])
k=0
for x in sp:
    x=''.join(x)
    if x[0]!='0' and int(x, 9)%2==0:
        if x.count('0')+x.count('2')+x.count('4')\
                +x.count('6')+x.count('8')<=2:
            k+=1
print(k)
