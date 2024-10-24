with open('24_6094.txt') as f:
    f = f.readline()
    f = f.replace('XYZY', '$')
k = 0
maxx = 0
f = f.replace('X', '*')
f = f.replace('Z', '*')
f = f.replace('*Y', '@')
for i in range(len(f)):
        if f[i] == '@':
            k += 1
            maxx = max(maxx, k)
        else:
            k = 0
print(maxx+1)
t=open('1.txt', 'w')
t.write(f)