k=0
def f(n):
    global k
    k=k+1
    if n>=1:
        k+=1
        f(n-1)
        f(n//2)
    return k
print(f(140))
