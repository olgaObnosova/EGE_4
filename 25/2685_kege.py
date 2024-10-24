def dl(n):
    d=set()
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            d.add(i)
            d.add(n//i)
    return d
k=0
for i in range(12*10**5, 0, -1):
    sm=dl(i)
    if len(sm)<2:
        sm=0
    else:
        sm=sum(sm)
    if sm!=0 and sm%2022==0:
        k+=1
        print(i, sm)
    if k==8:
        break