with open('27.txt') as f:
    ost = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    co = 0
    for i in f.readlines():
        a = int(i.strip('\n'))
        k = 0
        st = a % 4
        while a % 3 == 0:
            k += 1
            a //= 3
        k = min(k, 10)
        for j in ost[(4 - st) % 4][10 - k:]:
            co += j
        ost[st][k] += 1
    print(co)