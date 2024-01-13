with open('4685_A.txt') as f:
    n, m = map(int, f.readline().split())
    sp=[int(x)//6+bool(int(x)%6) for x in f]
s=sum(sp)
for i in range(len(sp)):

