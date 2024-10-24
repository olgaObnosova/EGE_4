'''
with open('27A-6.txt') as f:
    sp=[int(x) for x in f]
n=len(sp)
maxx=0
for i in range(n):
    for j in range(i+731, n):
        for p in range(j+731, n):
            maxx=max(maxx, sp[i]*sp[j]*sp[p])
print(maxx)
'''
with open('27A-6.txt') as f:
    sp=[int(x) for x in f]
k=731
maxxo=maxxo2=float('inf')
maxx=maxs=max3=max1p=maxxp=0
for i in range(0, len(sp)-2*k):
    maxxp=max(maxxp, sp[i]) #+
    maxxo= min(maxxo,sp[i]) #-
    #print(maxxp, maxxo)
    if sp[i+k]>0:
        max1p=max(max1p, (maxxp*sp[i+k]))#+
        maxxo2=min(maxxo2, maxxo*sp[i+k])
        #print(max1p, maxxo2)#-
    if maxxo2!=float('inf'):
        max3=max(max3, (max1p*sp[i+2*k]), maxxo2*sp[i+2*k])

print(max3)