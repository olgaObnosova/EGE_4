def f(a, h, ph):
    if a >=82:
        return (h) % 2 == (ph) % 2
    elif h == ph:
        return 0
    comb = [f(a + 10, h + 1, ph), f(a * 2, h + 1, ph)]
    return any(comb) if (h) % 2 == ph % 2 else all(comb)


for a in range(1, 72):
        if f(a, 0, 2):
            print(a)
print(bin(136), bin(151))