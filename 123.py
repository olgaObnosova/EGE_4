with open('1.txt') as f:
    f=f.readline()
k=1
maxx=0
s=f[0]
for i in range(len(f)-1):
    if f[i]>f[i+1]:
        s+=f[i+1]
        if len(s)>maxx:
            maxx=len(s)
            otv = s
    else:
        s=f[i]
print(maxx)# krqjWRC1 AAAAAA **AA ***
print(otv)
