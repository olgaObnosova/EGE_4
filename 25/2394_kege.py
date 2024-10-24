def dl(n):
    d=set()
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            d.add(i)
            d.add(n//i)
    return d
def pr(n):
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True
k=0
for i in range(67*10**4, 67*10**5):
    s = dl(i)
    sm=0
    for x in s:
        if pr(x):
            sm+=x
    if sm%10==5:
        k+=1
        print(i, sm)
    if k==5:
        break