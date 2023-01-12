with open('27-A-FARM.txt') as f:
    n, m, k = map(int, f.readline().split())
    sp1 = []
    sp2 = []
    for i in range(k):
        sp1.append(int(f.readline()))
    for i in range(k):
        sp2.append(int(f.readline()))
    count = 0
    print(sp1, sp2)
    for line in f:
        if sum(sp1) + sum(sp2) >= m:
            count += 1
        for i in range(len(sp1) - 1):
            sp1[i] = sp1[i + 1]
        sp1[len(sp1) - 1] = sp2[0]
        for i in range(len(sp2) - 1):
            sp2[i] = sp2[i + 1]

        sp2[len(sp2) - 1] = int(line)
        print(sp1, sum(sp1),sp2, sum(sp2))
if sum(sp1) + sum(sp2) >= m:
    count += 1
print(count)
