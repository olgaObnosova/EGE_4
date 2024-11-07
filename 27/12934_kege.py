with open('27-A_12934.txt') as f:
    k = int(f.readline())
    n = int(f.readline())
    sp = [int(x) for x in f]
maxx =s= cnt=0
otv=[]
print(k)
for i in range(n -1):
    s=cnt=0
    otv=[]
    for j in range(i, n):
        if s+sp[j] < k:
            s+=sp[j]
            cnt+=1
            maxx = max(maxx,cnt)
        else:
            break

print(maxx)
