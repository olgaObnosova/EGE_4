F = open("27_A_yan.txt")

N, K = map(int, F.readline().split())
sp = sorted([list(map(int, F.readline().split())) for i in range(N)])
a = [0] * K
for i in sp:
    a[i[0] % K] = bool(i[1] % 2) + i[1] // 2
#print(a[314])
p = [0] + [0] * 2 * K
for i in range(1, len(p)):
    p[i] = p[i - 1] + a[(i - 1) % K]
s = [(sum(a[i] * min(i, K - i) for i in range(K)), 0)]
#print(s)
for i in range(1, K):
    s += [(s[-1][0] + (p[i + K] - p[i + K // 2])\
           - (p[i + K // 2] - p[i]), i)]
#print(s)

t= min([x[0] for x in s])
for x in s:
    if x[0]==149799:
        print(x)