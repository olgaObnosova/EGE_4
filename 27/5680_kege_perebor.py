with open('5680_A.txt') as f:
    sp = []
    n, m, l = map(int, f.readline().split())
    for line in f:
        sp.append(int(line))
sp = sp + sp
#print(sp)
minn = float('inf')
for i in range(len(sp)//2):
    st = 0
    for j in range(i, len(sp)):
        if m <= j-i <= l:
            st += sp[j]*(j-i)
    #print(st, i)
    minn = min(minn, st)
print(minn)