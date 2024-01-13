with open('24_8510.txt') as f:
    f=f.readline()

k=1
maxx=0
z='NOP'
for i in range(len(f)):
    if not(f[i]  in z and f[i+1]  in z):
        k+=1
        maxx=max(maxx,k)
    else:
        k=1
print(maxx)