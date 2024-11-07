def f(n):
    s=set()
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            if i%10==7 and i!=7:
                s.add(i)
            if n//i%10==7 and n//i!=7:
                s.add(n//i)
    return list(s)
k=0
for i in range(700_001, 10**8):
    d=f(i)
    if len(d)!=0:
        k+=1
        print(i, min(d))
        if k==5:
            break