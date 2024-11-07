
def f(a, h, ph):
    if a <= 19:
        return h%2==ph%2
    elif h==ph:
        return False
    comb = [f(a-2, h + 1, ph), f(a - 5, h + 1, ph), f(a//3, h + 1, ph)]
    return any(comb) if (h+1)%2==ph%2 else all(comb)
for a in range(100, 20, -1):
    if f(a, 0, 3):
        print(a)