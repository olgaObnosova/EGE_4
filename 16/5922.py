sp = [0] * 10_001
sp[10_000] = 1
for i in range(11):
    sp[i] = i
for i in range(9998, 0, -2):
    sp[i] = i % 10 + sp[i + 2]
for i in range(11, 10_000, 2):
    sp[i] = sp[i - 2] - (i - 1) % 10
print(sp[4500] + sp[5515])
