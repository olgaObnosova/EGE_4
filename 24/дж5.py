with open('24-7.txt') as f:
    f = f.readline()
    f = f.replace('EA','**')
    f = f.replace('NPC', '***')
    k = 0
    maxx = 0
for x in f:
    if x=='*':
        k+=1
        maxx=max(maxx, k)
    else:
        k=0
print(maxx)

