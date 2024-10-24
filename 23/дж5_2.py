def f(st, e):
    if st>e:
        return 0
    elif st==e:
        return 1
    return f(st+3, e)+f(st*3, e)
k=0
sr=[]
for i in range(11,100,2):
    d = f(10,i)
    print(d, i)
    if d:
        sr.append(i)
        k+=1
print(k)
