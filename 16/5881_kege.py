def f(n):
    if n<10:
        return 0
    else:
        return f(n//10) + (n//10%10)-(n%10)
k=0
for i in range(10**10):
    if f(i)==9:
        k+=1
print(k)