def d(n):
    s=set()
    for i in range(1, int(n**0.5)+1):
        if n%i==0:
            if i%2==0:
                s.add(i)
            if n//i%2==0:
                s.add(n//i)
    return s
import fnmatch as f
k=0
for i in range(65001, 10**9):
    t=d(i)
    if f.fnmatch(str(i),'6*97*5?') and len(t)>=4:
        k+=1
        print(i,sum(t))
        if k==7:
            break