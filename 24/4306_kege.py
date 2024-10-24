with open('24_4306.txt') as f:
    f=f.readline()
    f=f.split('R')

maxx=0
for x in f:
    x=x.split('A')
    for i in range(len(x)):
        sr=x[i:i+4]
        sr=''.join(sr)
        maxx=max(maxx, len(sr)+3)
print(maxx)