
def delit(n):
    s=set()
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            s.add(i)
            s.add(n//i)
    return list(s)
print(delit(17))
k=0
for i in range(800_000, 8_000_000):
    t = delit(i)
    if len(t)>0 and (min(t)+max(t))%10==4:
        print(i,min(t)+max(t))
        k+=1
    if k==5:
        break

