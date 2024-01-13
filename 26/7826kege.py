with open('26_7826.txt') as f:
    k,n = map(int, f.readline().split())
    sp=[]
    for line in f:
        a, b = map(int, line.split())
        sp.append((a,b))
attr=[(0,0)]*k
sp.sort()
#print(sp)
pos=nom=0
for x in sp:
    fl=1
    for i in range(k):
        if attr[i][0]==x[0]:
            pos+=1
            fl=0
            attr[i]=x
            break
    if fl:
        for i in range(k):
            if x[0]>attr[i][1]:
                pos+=1
                nom=i
                attr[i] = x
                break
    #print(attr)
print(nom+1, pos)