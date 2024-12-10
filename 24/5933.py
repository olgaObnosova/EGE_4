with open('24-238.txt') as f:
    f = f.readline()
f = f.replace('DAD', '@@@')
k = maxk = n = 0
for x in f:
    if x == '@':
        k += 1
        maxk = max(maxk, k)
    else:
        k=0
print(maxk)