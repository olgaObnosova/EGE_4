with open('24_2715.txt') as f:
    f=f.readline()
f1=set(f)
sp=[]
for x in f1:
    sp.append([f.count(x), x])
sp.sort() # DEV мин
print(sp) # FIN макс