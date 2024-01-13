with open('26_11749_11749.txt') as f:
    kolo=int(f.readline())
    n=f.readline()
    sp=[]
    for x in f:
        a, b=map(int, x.split())
        sp.append((a,b))
sp.sort()
spo=[0]*kolo
k=0
k1080=0
k1200=0
for x in sp: # приш до 1080 и закончил до 1200
    st, end=x
    if st<=1080:
        k1080+=1
    if end<=1200:
        k1200+=1
    for i in range(kolo):
        if st>spo[i] and st<=1080:
            k+=1
            spo[i]=end
            otv=i
            break
print(k1080-k1200)
#print(spo)
print(otv+1)
