k = 0
def f(n):
    global k
    k+= 1
    if n>1:
        f(n-2)
        f(n//2)
        k+= 1
    k+= 1
    return k

print(f(127))