def f(a, b, h, ph):
    if a+b>=65:
        return h%2==ph%2
    elif h==ph:
        return False
    comb = [f(a+1,b,h+1, ph), f(a,b+1,h+1, ph),\
            f(a*3,b,h+1, ph), f(a,b*3,h+1, ph)]
    return any(comb) if (h+1)%2==ph%2 else all(comb)
for a in range(1, 59):
    if f(a, 6, 0, 3):
        print(a)