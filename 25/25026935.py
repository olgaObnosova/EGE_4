import fnmatch as f
def sm(n):
    s=0
    for x in str(n):
        s+=int(x)
    return s
for i in range(2023,10**9,2023):
    if f.fnmatch(str(i),'20*23'):
        r=sm(i)
        if r<20 and r%7==0:
            print(i)