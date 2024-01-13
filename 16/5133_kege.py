sp = [0] * 2049
for i in range(2049):
    if i < 3:
        sp[i] = 1
    if i > 2 and i % 2 == 0:
        sp[i] = sp[i - 1] + i - 1
    if i > 2 and i % 2 != 0:
        sp[i] = sp[i - 2] + 2 * i - 2
print(sp[2048] - sp[2045])
