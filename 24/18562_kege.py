with open('24_18562.txt') as f:
    f=f.readline()

f=f.split('XYYYZ')
maxl=0
sp=[]
for x in f:
    sp.append((len(x), x))
sp.sort(reverse=True)
print(f.index(sp[0][1]), len(sp[0][1])+4)
print(f.index(sp[1][1]),  len(sp[1][1])+8)
print(f.index(sp[2][1]), len(sp[2][1])+8)


