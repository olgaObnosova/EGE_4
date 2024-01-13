with open('27-6799b.txt') as f:
    n, k = map(int, f.readline().split())
    sp=[0]*(k)
    otv=ch=bk=0
    for line in f:
        x=int(line)
        if x>=k:
            otv+=ch
            bk+=1
        else:
            otv+=sum(sp[k-x+1:])+bk
            sp[x]+=1
        ch+=1
print(otv)
#print(sp)

