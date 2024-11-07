import fnmatch as f
def pr(n):
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True
for i in range(1, 10**7, 1):
    if pr(i) and f.fnmatch(str(i), '3?1111*'):
        print(i)