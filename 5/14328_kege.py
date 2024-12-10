
def f(n):
    st = '0123456789AB' #22 1A
    s = ''
    while n!=0:
        s+=str(st[n%12]) #st[10]
        n=n//12
    return s[::-1]
maxx = 0
for i in range(1000):
    n = f(i)
    if i%3==0:
        n = '1' + n +'B'
    else:
        n = '2' + n + '0'
    r = int(n, 12)
    if r < 1996:
        maxx = max(maxx, r)
print(maxx)