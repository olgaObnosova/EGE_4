maxx=0
s=0
for n in range(101, 1000):
    a='1'*n
    while '333' in a or '111' in a:
        a = a.replace('333', '11', 1)
        a = a.replace('111', '3', 1)
    if maxx < int(a):
        maxx=int(a)
        s=n
print(maxx, s)