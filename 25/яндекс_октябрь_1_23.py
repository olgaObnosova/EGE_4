def f(n):
    s=set()
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            s.add(i)
            s.add(n//i)
    return s
k = 0
for i in range(123457,10**10):
    d = f(i)
    if len(d)==4:
        k+=1
        print(i, sum(d))
    if k == 5:
        break

