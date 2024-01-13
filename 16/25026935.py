def f(n):
    if n<9:
        return n//3+n%3
    return f(n//9)+f(n%3)
for i in range(10**9,10**8,-1):
    if f(i)==33:
        print(f(i),i)