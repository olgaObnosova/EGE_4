with open('17_12926.txt') as f:
    sp = []
    maxx = 0
    for x in f:
        sp.append(int(x))
        if len(str(abs(int(x)))) == 2:
            maxx = max(maxx, int(x))
k = 0
print(maxx)
minn = float('inf')
A = -float('inf')
for i in range(len(sp) - 3):
    if abs(sp[i]) % 10 == abs(sp[i + 1]) % 10 == abs(sp[i + 2]) % 10 == abs(sp[i + 3]) % 10:
        #print(sp[i], sp[i + 1], sp[i + 2], sp[i + 3])
        A = max(A, sp[i] + sp[i + 1] + sp[i + 2] + sp[i + 3])
print(A)
for i in range(len(sp) - 4):
    l = 0
    if sp[i] < A:
        l += 1
    if sp[i + 1] < A:
        l += 1
    if sp[i + 2] < A:
        l += 1
    if sp[i + 3] < A:
        l += 1
    if sp[i + 4] < A:
        l += 1
    if l == 1 and (sp[i] + sp[i + 1] + sp[i + 2] + sp[i + 3] + sp[i + 4]) % maxx == 0:
        k += 1
        minn = min(minn, sp[i] + sp[i + 1] + sp[i + 2] + sp[i + 3] + sp[i + 4])
print(k, minn)