with open('24_12410.txt') as f:
    f=list(f.readline())
n=len(f)
for i in range(1, n):
    if f[i]<f[i-1]:
        f[i]='*'
f=''.join(f)
f=f.split('*')
maxx=0
for i in range(n-100001):
    s='*'.join(f[i:i+100001])
    maxx=max(maxx, len(s))
print(maxx)