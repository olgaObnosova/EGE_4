with open('24_8959.txt') as f:
    f=f.readline()
f=f.replace('EA','**')
f=f.replace('NPC','***')
k=maxk=0
for x in f:
    if x=='*':
        k+=1
        maxk=max(maxk,k)
    else:
        k=0
print(maxk)