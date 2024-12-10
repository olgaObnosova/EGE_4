def f(a, b, h, ph):
    if a+b >=231:
        return h % 2 == ph % 2
    elif h==ph:
        return False
    comb = [f(a+4, b, h+1, ph),f(a, b+4, h+1, ph),\
            f(a*3, b, h+1, ph),f(a, b*3, h+1, ph)]
    return any(comb) if (h+1)%2==ph%2 else all(comb)
for i in range(1, 218):
    if f(10, i, 0, 4) and not f(10, i, 0, 2):
        print(i)