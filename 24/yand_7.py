with open('24-8.txt') as f:
    f = f.readline()
k=0
f=f.split('AHAHA')
maxx=0
for x in f:
    if len(x)>maxx:
        maxx=len(x)
        s=x
        otv=k
    k+=1
print(maxx+2+4, otv, len(f))
print(s[:5], s[-5:]) #AHAHA
