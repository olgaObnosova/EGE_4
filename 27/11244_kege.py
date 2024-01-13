with open('27_A_11244.txt') as f:
    k = int(f.readline())
    n = int(f.readline())
    sp = [int(x) for x in f]
maxx = 0
for i in range(n):
    for j in range(i+1, n):
        if abs(i-j) % k == 0:
            maxx = max(maxx, sp[i]*sp[j])
print(maxx)
