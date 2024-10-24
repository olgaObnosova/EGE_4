with open('27-proege_6_b.txt') as f:
    n, k = map(int, f.readline().split())
    sp = [int(x) for x in f]

cnt=0
sp1=sp[:len(sp)//2]
sp2=sp[len(sp)//2:]
print(sp1[-1])
print(sp2[0])
for i in range(len(sp)//2):
    if sp1[i]+sp2[len(sp2)-i-1]<k:
        cnt+=1
    else:
        cnt+=1
print(cnt)
