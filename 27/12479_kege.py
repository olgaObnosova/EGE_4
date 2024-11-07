with open('27-A_12479.txt') as f:
    k = int(f.readline())
    n = int(f.readline())
    sp = [int(x) for x in f]
maxx = 0
for i in range(n-k):
    for j in range(i + k, n):
        maxx = max(maxx, sp[i] + sp[j] + abs(i-j))
print(maxx)
