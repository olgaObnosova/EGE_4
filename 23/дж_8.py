def f(st,e,k):
    if st>e or k > 5:
        return 0
    elif st==e:
        return 1
    return f(st+1, e, k+1) +f(st*2, e, k+1)+f(st+st%4, e, k+1)
k=0
for i in range(100):
    g=f(i, 80, 0)
    if g:
        k+=1
print(k)