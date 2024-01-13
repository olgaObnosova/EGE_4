with open('27_B_11244.txt') as f:
    k = int(f.readline())
    n = int(f.readline())
    ind = 0
    sp=[]
    for x in f:
        sp.append((int(x), ind))
        ind+=1
sp.sort()
print(k)
print(sp[:10])
