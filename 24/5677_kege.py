with open('5677.txt') as f:
    f = f.readline()
f = f.replace('DAD','*')
maxx = k = 0
for i in range(len(f)):
    if f[i] == '*':
        k += 1
        if k > maxx:
            maxx = k
            a = i
    else:
        k = 0
        n = i
print(maxx*3+3)
print(f[a-k-3:a+4])
print(f[a-maxx-4:a])

