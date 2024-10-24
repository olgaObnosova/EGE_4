def f(n):
    if n <= 2:
        return  1
    if n > 2 and n % 2 !=0:
        return  f(n - 1) - n
    if n > 2 and n % 2 == 0:
        return f(n - 2) - f(n - 1) + 2
print(f(27))

a=322

print(a%10==a%100//10)