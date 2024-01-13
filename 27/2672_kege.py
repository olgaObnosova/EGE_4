i6 = 0
i3 = 0
i2 = 0
i1 = 0
o = 0
k=r=0
with open('27-12b.txt') as f:
    a = f.readline()
    for line in f:
        line = int(line)
        if line % 6 == 0:
            k+=r
            i6 += 1
        elif line % 3 == 0:
            k+=i2+i6
            i3 += 1
        elif line % 2 == 0:
            k+=i3+i6
            i2 += 1
        else:
            k+=i6
            i1 += 1
        r+=1
print(i1, i2, i3, i6)
print(i1 * i6 + i2 * i3 + i6 * 0.5 * (i6 - 1) + i6 * i2 + i6 * i3)