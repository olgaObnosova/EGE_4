with open('27B_25017844.txt') as f:
    n = int(f.readline())
    s = 0
    sp = []
    maxx = 0
    for line in f:
        sp.append(int(line))
        s += int(line)
# print(sp[0])
for i in range(len(sp) - 3):
    #print(sp[i:i + 3])
    # break
    if s - sum(sp[i:i + 3]) > maxx \
            and (s - sum(sp[i:i + 3])) % 13 == 0:
        maxx = s - sum(sp[i:i + 3])

print(maxx)

