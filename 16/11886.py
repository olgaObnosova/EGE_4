def f(n):
    return g(n-1)
def g(n):
    if n<10:
        return n
    else:
        return g(n-2)+1
k=0
for i in range(1, 101):
    t = f(i)
    if t > 0 and t**0.5==int(t**0.5):
        k+=1
        print(t, i)
print(k)