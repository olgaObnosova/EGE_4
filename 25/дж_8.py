def fr(n):
    s=0
    for x in str(n):
        s+=int(x)
    return s
k=0
import fnmatch as f
for i in range(700_011, 10**8, 13):
    if not(f.fnmatch(str(i),'*0??3*')) and \
            not (f.fnmatch(str(i), '*4??2')) \
            and not(f.fnmatch(str(i),'*1*')):
        k+=1
        print(i, fr(str(i)))
        if k>5:
            break