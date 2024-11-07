
def F(n):
    global k
    k+=1
    if n > 1:
        F(n - 2)
        F(n // 2)
        k+=1
    k+=1
    return k
k = 0
print(F(127))

