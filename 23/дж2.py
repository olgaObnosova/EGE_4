def f(start, stop, l):
    if start > stop:
        return 0
    elif start==stop and l==5:
        return 1
    elif start==stop and l!=5:
        return 0
    elif start<stop:
        return f(start+4, stop,l+1) + f(start*2, stop, l+1)
s = set()
for i in range(3, 100):
    d = f(2,i,0)
    if d:
        s.add(i)
print(len(s))