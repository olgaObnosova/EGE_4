def f(n):
    if n<3:
        return n
    if n>2 and n%2!=0:
        return f(n-1)+f(n-2)+1
    if n > 2 and n % 2 == 0:
        return sum([f(x) for x in range(1, n)])
print(f(10))
