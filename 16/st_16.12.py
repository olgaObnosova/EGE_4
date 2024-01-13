def f(n):
    if n==0:
        return 0
    elif n>0 and n%2==0:
        return f(n//10)+n%10
    return f(n//10)
k=0
for i in range(1, 104):
    print(f(i), i)
