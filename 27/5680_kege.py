with open('5680_A.txt') as f:
    sp = []
    n, m, l = map(int, f.readline().split())
    for line in f:
        sp.append(int(line))
