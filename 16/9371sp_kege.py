import sys
sys.setrecursionlimit(3000)
def f(n):
    if n >=3210:
        return 1
    return f(n+3)+7
def g(n):
    if n <10:
        return n
    return g(n-3)+5
print(g(3000))
