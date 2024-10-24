with open('24_5139.txt') as f:
    f=f.readline()
f=f.replace('C','B')
f=f.replace('D','B')
f=f.replace('F','B')
f=f.replace('E','A')
f=f.replace('U','A')
f=f.replace('BAB','*')
k=maxx=0
for x in f:
    if x=='*':
        k+=1
        maxx=max(maxx, k)
    else:
        k=0
print(maxx)