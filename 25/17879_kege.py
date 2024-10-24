def delit(n):
    m = 0
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            m+=i
            m+=n//i
            break
    return m
k=0
for i in range(800_001, 1_000_000):
    t = delit(i)
    if t%10==4:
        print(i, t)
        k+=1
    if k==5:
        break
