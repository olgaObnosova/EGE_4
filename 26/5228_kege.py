with open('5228.txt') as f:
    n = f.readline()
    sp = []
    for line in f:
        sp.append(int(line))
sp.sort(reverse=True)
k = 1
a = sp[0]
for i in range(1, len(sp) - 1):
    if a - sp[i] >= 8:
        k += 1
        a = sp[i]
# print(sp)
print(k)
print(a)