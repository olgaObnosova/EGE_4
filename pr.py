n = 0
ch = []
with open('pr') as f:
    e = f.readline().split()
    k = int(e[-1])
    n1 = int(e[0])
    sp = [0] * k
    sd = 0
    for line in f:
        sd += 1
        x = int(line)
        ch.append(x)
        if x < k:
            sp[x] += 1
        else:
            n += sd - 1 # 0 1 2 3 4 5 6 7 8 9
if k % 2 == 0:
    n += sp[len(sp)//2] * (sp[len(sp)//2:] - 1) // 2
    print(n)
    for i in range(len(sp) // 2):
        n += sp[i] * sum(sp[-(i):])
else:
    for i in range(len(sp) // 2 + 1):
        n += sp[i] * sum(sp[-(i):])
print(n)



