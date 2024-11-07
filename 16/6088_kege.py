sp = [0] * 3003
for i in range(len(sp)-1, -1,-1):
    if i > 3000:
        sp[i] = 1
    elif i <= 3000 and i % 2 == 0:
        sp[i] = sp[i + 1] - i + 1
    else:
        sp[i] = sp[i + 2] - 2 * i + 2
print(2 * sp[39] - 2 * sp[34])