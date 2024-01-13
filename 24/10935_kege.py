with open('24_10935.txt') as f:
    f = f.readline().split('U')
maxl = 0
maxstr = ''
for i in range(1,len(f)-1):
    if len(f[i]) > maxl:
        maxl = len(f[i])
        maxstr = f[i]
symv=set(maxstr)
for x in symv:
    print(x, maxstr.count(x))

