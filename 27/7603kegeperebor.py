with open('27A_7603.txt') as f:
    n = int(f.readline())
    k = int(f.readline())
    sp=[int(x) for x in f]
mx=0
for i in range(len(sp)-k):
    for j in range(i+k,len(sp)):
        mx=max(mx, sp[i]+sp[j])
print(mx)
