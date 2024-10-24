def f(a, h, ph):
    if 50<=a<=119:
        return h%2==ph%2
    elif h==ph:
        return 0
    comb=[f(a+2, h+1, ph), f(a*3, h+1, ph)]
    return any(comb) if (h+1)%2==ph%2 else all(comb)

for a in range(45, 49):
    if f(a, 0, 2):
        print(a)