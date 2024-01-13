def dl(n):
    d = set()
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            d.add(i)
            d.add(n//i)
    return d
def pr(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
import fnmatch as f
for i in range(10**10, 1000,-1):
    if f.fnmatch(str(i),'1*3?9'):
        t = dl(i)
        #print(t)
        if pr(sum(t)):
            print(i, t)


