def delit(n):
    s=set()
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            s.add(i)
            s.add(n//i)
    return len(s)

def pr(n):
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

import fnmatch as f
for i in range(100001792, 10**9, 2024):
    if f.fnmatch(str(i), '1*3*'):
        t=delit(i)
        if pr(t):
            print(i, i//2024)
