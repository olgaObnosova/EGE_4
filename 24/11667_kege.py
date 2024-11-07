with open('24_11667.txt') as f:
    f=f.readline()
    f=f.split('INFINITY')

maxx=0
for i in range(0, len(f)-1001):
    s='INFINITY'.join(f[i:i+1001])
    a=len(s)
    if a>maxx:
        maxx=max(maxx, a)
        otv=s
print(maxx+14)