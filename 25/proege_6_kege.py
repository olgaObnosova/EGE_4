def dl(n):
    s=set()
    for i in range(1, int(n**0.5)+1):
        if n%i==0:
            s.add(i)
            s.add(n//i)
    return s
for i in range(123456,987655):
    t=dl(i)
    if len(t)==5:
        t=list(t)
        t.sort()
        print(t[-2:])
print(6028+5026)