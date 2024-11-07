with open('24_12931.txt') as f:
    f=f.readline()
    f=f.replace('VWXYZ','*****')
    z = open('2.txt', 'w')
    z.write(f)
k=maxx=0
for x in f:
    if x=='*':
        k+=1
        maxx=max(maxx, k)
    else:
        k=0
print(maxx)

