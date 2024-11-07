def f(n):
    s=set()
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            s.add(i)
            s.add(n//i)
    return s
k=0
print(f(18))
for i in range(424242, 10**7):
    d=f(i)
    if len(d)>0:
        m=min(d)+max(d)
        if m%2024==42:
            k+=1
            print(i, m)
            if k==8:
                break