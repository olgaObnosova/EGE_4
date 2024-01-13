def f(n):
    n=str(n)
    for i in range(2):
        if n[i]!=n[i+1]:
            return False
    return True
print(f(912))
