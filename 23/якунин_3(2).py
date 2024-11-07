def pr(x, y):
    if y == 0:
        sum = 0
        for i in str(x):
            sum += int(i)
        return int(x + sum)
    if y == 1:
        z = str(x)
        strk = ''
        for i in z[:-1]:
            strk += i
        return int(str(z[-1] + strk))
otv = []
for i1 in range(2):
    for i2 in range(2):
        for i3 in range(2):
            for i4 in range(2):
                for i5 in range(2):
                    for i6 in range(2):
                        for i7 in range(2):
                            for i8 in range(2):
                                for i9 in range(2):
                                    for i10 in range(2):
                                        for i11 in range(2):
                                            for i12 in range(2):
                                                for i13 in range(2):
                                                    for i14 in range(2):
                                                        for i15 in range(2):
                                                            otv.append(pr(pr(pr(pr(pr(pr(pr(pr(pr(pr(pr(pr(pr(pr(pr(15, i1), i2), i3), i4), i5), i6), i7), i8), i9), i10), i11), i12), i13), i14), i15))
otv = set(otv)
print(len(otv))