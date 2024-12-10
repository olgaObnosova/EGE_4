def f(a, b, h, ph):
    if a+b <=72:
        return h%2==ph%2
    elif h==ph:
        return 0
    comb=[f(a-3, b, h+1, ph),f(a, b-3, h+1, ph),\
          f(a//2 + a%2, b, h+1, ph),f(a, b//2+b%2, h+1, ph)]
    return any(comb) if (h+1)%2==ph%2 else all(comb)
for i in range(200, 22, -1):
    if f(i, 50, 0, 4) and not f(i, 50, 0, 2):
        print(i)