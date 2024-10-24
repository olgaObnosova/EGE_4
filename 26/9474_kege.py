with open('26_9474.txt') as f:
    k = int(f.readline())
    n = int(f.readline())
    sp=[]
    for x in f:
        a, b = map(int, x.split())
        sp.append([a,b])
sp.sort()
okn=[0]*k
cnt=0
otv=0
for x in sp: # [1, 50]
    st, end = x
    #print(okn)
    for i in range(k):
        minn=min(okn)
        if okn[i]==minn and okn[i]<=end-1:
            okn[i] = end
            #print(okn)
            cnt+=1
            otv=i
            break
print(cnt, otv + 1)
print(k)



