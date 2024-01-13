with open('24.txt') as f:
    f=f.readline()
ch='02468'
nc='13579'
maxx=0
k=1
for i in range(len(f)):
    if not((f[i] in ch and f[i+1] in nc)\
           or(f[i] in nc and f[i+1] in ch)):
        k+=1
        maxx=max(maxx,k)
    else:
        k=1
print(maxx)