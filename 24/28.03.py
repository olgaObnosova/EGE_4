with open('24.txt') as f:
    f=f.readline().split('A')
maxx=0
#print(f[0])
for x in f:
    #print(x)
    if x.count('D')>0:
        x=x.split('D')
        #print(x)
        maxx=max(maxx,len(x[0]))
        maxx = max(maxx, len(x[-1]))
print(maxx)
