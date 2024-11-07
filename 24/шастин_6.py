with open('24-8.txt') as f:
    f=f.readline()
for x in '34ABCDE':
    f=f.replace(x, '*')
f=f.split('*')
#print(f[:2])
k = 0
for x in f:
    c = 0
    if len(x)>0 and x[0]!='0':
        for y in x:
            c+=1
            k+=c
        k=k-x.count('0')
    elif len(x)>0:
        for y in x[1:]:
            c+=1
            k+=c
        k = k - x.count('0') + 1

print(k)



