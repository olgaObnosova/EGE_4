def f(a, h, ph):
    if a >= 108:
        return h % 2 == ph % 2
    elif h == ph:
        return False
    comb = [f(a + 1, h + 1, ph), f(a *(1.5+0.5*(a%2)),\
                                   h + 1, ph)]
    return any(comb) if (h + 1) % 2 == ph % 2\
        else all(comb)


for a in range(1, 108):
    for ph in range(5):
        if f(a, 0, ph):
            if ph == 2:
                print(a)
            break