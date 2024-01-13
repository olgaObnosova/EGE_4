def f(n):
    if n<2:
        return n
    else:
        return f(n//2)*10+n%2
'''for i in range(20):
    print(i, f(i))'''
print(int('100000100001000100101', 2))