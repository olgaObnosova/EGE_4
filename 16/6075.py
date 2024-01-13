def f(n):
    if n==0:
        return 0
    return f(n//10)+n%10
for i in range(1,100):
    print(i, f(i))