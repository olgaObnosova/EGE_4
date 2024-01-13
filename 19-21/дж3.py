def f(a, s, h, ph):
    if a + s >= 57:
        return h % 2 == ph % 2
    elif h == ph:
        return 0
    comb = [f(a + s, s, h + 1, ph), f(a, s + a, h + 1, ph) ]
    return any(comb) if (h + 1) % 2 == ph % 2 else all(comb)


for s in range(1,100):
    for ph in range(5):
        if f(s, s, 0, ph):
            if ph == 4:
                print(s)
            break