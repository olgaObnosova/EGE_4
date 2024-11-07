with open('24-7.txt') as f:
    f=f.readline()
    f=f.replace('XZZY', '*')
k=0
maxx=0
s=''
for i in range(len(f)):
    if f[i]!='*':
        s+=f[i]
        k+=1
        if k>maxx:
            maxx=max(maxx, k)
            otv=s
    else:
        k=0
        s=''

print(maxx)
print(s)