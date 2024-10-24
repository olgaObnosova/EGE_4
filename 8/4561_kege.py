import itertools as t
comb= list(t.product('ПОЛЯКВ', repeat=4))
k=0
for x in comb:
    l = 0
    x = ''.join(x)
    if x[0]=='В': # if x.find('В')==0:
        l+=1
    if x[1]=='О':
        l+=1
    if x[2]=='Л':
        l+=1
    if x[-1]=='К':
        l+=1
    if l==2:
        k+=1
print(k)

