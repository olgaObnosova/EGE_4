sp = [0] * 10_002
for i in range(10_001, 9000, -1):
    if i >= 10_000:
        sp[i] = i
    elif i % 2 == 0:
        sp[i] = sp[i + 1] + i ** 2 - 3 * (i - 1)
    else:
        sp[i] = sp[i + 2] + 4 * i + 1
print(sp[9950]-sp[9999])