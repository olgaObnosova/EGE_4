with  open('26-18.txt') as f:
    k, n =map(int,f.readline().split())
    sp=[int(x) for x in f]
sp.sort()
ch=[0]*k
cnt=0
chk=[0]*k
for x in sp:
    for i in range(k):
        if x>=ch[i]:
            ch[i]=x+60
            chk[i]+=1
            cnt+=1
            break
    #print(ch)
print(cnt)
print(min(chk))