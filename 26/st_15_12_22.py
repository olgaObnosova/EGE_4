with open('26_15_12_22.txt') as f:
    a = []
    b = []
    for line in f:
        line = line.split()
        if line[1] == 'A':
            a.append(int(line[0]))
        else:
            b.append(int(line[0]))
a.sort()
b.sort()


