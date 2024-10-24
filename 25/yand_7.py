def f(n):
    s=set()
    for i in range(2,int(n**0.5)+1): #100 10 2
        if n%i==0:
            if i%2==0:
                s.add(i)
            if (n//i)%2==0:
                s.add(n//i)
    return s
for i in range(397438, 443521):
    d=f(i)
    if len(d)>=142:
        print(len(d), max(d))
