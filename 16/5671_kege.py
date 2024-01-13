sp = [0] * 10_010
for i in range(11):
    sp[i] = i
for i in range(10_009, 9999, -1):
    sp[i] = 1
for i in range(11, 10_001, 2):
    sp[i] = sp[i - 2] - (i - 1) % 10
for i in range(10_000, 10, -2):
    sp[i] = sp[i + 2] + i % 10
print(sp[4500] + sp[5515])
