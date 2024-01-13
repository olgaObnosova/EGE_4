with open('2660B') as f:
    n = int(f.readline())
    s = 0
    minr = float('inf')
    for line in f:
        a, b = map(int, line.split())
        s+= max(a, b)
        if abs(a-b)%3!=0:
            minr=min(minr,abs(a-b))
if s%3!=0:
    print(s)
else:
    print(s-minr)
