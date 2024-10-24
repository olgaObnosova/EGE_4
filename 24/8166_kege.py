with open('24_8166.txt') as f:
    f = f.readline()
    f = f.replace('A', '*')
    f = f.replace('B', '*')
    f = f.replace('C', '*')

k = 0
maxx = 0
for i in range(len(f)-1):
    if f[i] == '*' and f[i+1]=='*':
        k += 1
        maxx = max(maxx, k)
    else:
        k = 0
print(maxx//2)