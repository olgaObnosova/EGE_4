def tr(n):
    s=''
    while n!=0:
        s+=str(n%3)
        n=n//3
    return s[::-1]
for i in range(1, 100):
    n = tr(i)
    if i%2==0:
        n = '1'+ n + '00'
    else:
        s = tr(n.count('1') + n.count('2')*2)
        n = n + s
    r = int(n, 3)
    if r > 168:
        print(i)

print(5*8*7*7*7-13377)
print(7**3)




