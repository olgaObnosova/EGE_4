def delit(n):
    s=set()
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            s.add(i)
            s.add(n//i)
    if len(s)==0:
        return 0
    return max(s)+min(s)
a=input()
if a==a[::-1]
'''
import fnmatch as f
for i in range(512034, 10**8):
    if f.fnmatch(str(i),'51*2?34'):
        t = delit(i)
        if t!=0 and t%117==0:
            print(i, t)
'''