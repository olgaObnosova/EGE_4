with open('24_7272.txt') as f:
    f=f.readline()
f=f.replace('AB','*')
f=f.replace('CB','*')
k=maxx=0
for x in f:
    if x=='*':
        k+=1
        maxx=max(maxx,k)
    else:
        k=0
print(maxx)

