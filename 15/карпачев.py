def f(n):
    n = bin(n)[2:]
    if n.count('1')%2 == 0:
        return True
    return False
b = range(100,191)
for x in range(190,99,-1):
    if f(x) and x in b and x%8==0:
        print(x)
        break
