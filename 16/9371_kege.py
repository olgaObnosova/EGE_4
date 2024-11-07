sp1 = [0] * 3220
for n in range(3219, 0, -1):
    if n >= 3210:
        sp1[n] = 1
    else:
        sp1[n] = sp1[n + 3] + 7
sp2 = [0] * 3220
for n in range(1, 3220):
    if n < 10:
        sp2[n] = n
    else:
        sp2[n] = sp2[n - 3] + 5
print(sp2[3000])