with open('27_A_6.txt', 'r') as f:
    n, k = tuple(map(int, f.readline().split()))
    amm, trash = 1, 0
    #print(n, k)
    for x in f.readlines():
        trash += int(x)
        trash = max(0, trash)
        while trash > k * amm:
            amm += 1
    print(amm)
