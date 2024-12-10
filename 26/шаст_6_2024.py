with open('26-24_3.txt') as f:
    n=f.readline()
    sp=[[int(y) for y in x.split()] for x in f]
sp.sort(key=lambda x: x[1])
vr=[0]*1441
for x in sp:
    for i in range(x[1], x[2]):
        vr[i]+=1
s=max(vr)
otv=[]
for i in range(len(vr)):
    if vr[i]==s:
        otv.append(i)
k=1
maxx=0
print(otv)
for i in range(len(otv)-1):
    if abs(otv[i]-otv[i+1]) !=1:
       k+=1
print(k)
q=0 #963-970
