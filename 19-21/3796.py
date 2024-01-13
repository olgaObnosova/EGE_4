def f(a, b, h, ph):
    if a + b >= 68:
        return h % 2 == ph % 2
    elif h == ph:
        return 0
    pos = [f(a + 1, b, h + 1, ph), f(a, b + 1, h + 1, ph), \
           f(a + b, b, h + 1, ph), f(a, b + a, h + 1, ph)]
    return any(pos) if (h + 1) % 2 == ph % 2 else all(pos)


for b in range(1, 59):
    for ph in range(5):
        if f(8, b, 0, ph):
            if ph == 2:
                print(b)
            break
