with open('24_dos.txt') as f:
    f = f.readline()

maxx = 0
k = 1
bok = 'QRS'
for i in range(len(f)-1):
    if not (f[i] in bok and f[i + 1] in bok):
        k += 1
        maxx = max(maxx, k)
    else:
        k = 1
print(maxx)