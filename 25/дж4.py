import fnmatch as f
def fn(n):
    s=set()
    for i in range(1, int(n**0.5)+1):
        if n%i==0:
            if f.fnmatch(str(i),'4*'):
                s.add(i)
            if f.fnmatch(str(n//i), '4*'):
                s.add(n//i)
    return s
for i in range(10**6):
    d = fn(i)
    if len(d)==24:
        print(i, max(d))
