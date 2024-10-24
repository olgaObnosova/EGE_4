def delit(n):
    s=set()
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            s.add(i)
            s.add(n//i)
    return list(s)
k=0
for i in range(1_200_000, 100, -1):
    t=delit(i)
    t.sort()
    if len(t)>=3:
        s=sum(t[-3:])
        if s%2022==0 and s!=i:
            print(i, s)
            k+=1
            if k==5:
                break
sp=[1,20,3,5,15,45,90,60]
maxx=0
for i in range(len(sp)-1):
    for j in range(i+1, len(sp)):
        if (sp[i]*sp[j])%15==0 and (sp[i]*sp[j])%45!=0:
            maxx=max(maxx, sp[i]*sp[j])
