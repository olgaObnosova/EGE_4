with open('24_2684.txt') as f:
    sp=f.readline()
mn=set(sp)

itog=[]
for x in mn:
    k=sp.count(x)
    itog.append([k,x])
itog.sort()
print(itog)