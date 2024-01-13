def f(s, c, max_):
    if s > 128:
        return c % 2 == max_ % 2  # проверка хода именно одного игрока
    if c == max_:  # мы сделали нужное количество шагов? но так и не выиграли
        return 0
    if c % 2 != max_ % 2:
        return f(s + 1, c + 1, max_) or f(s * 2, c + 1, max_)
    else:
        return f(s + 1, c + 1, max_) and f(s * 2, c + 1, max_)


for x in range(1, 128 + 1):# Четный ход-Петя, Нечетный Ваня
    for j in range(1, 100):# 0-Всегда
        if f(x, 0, j): #64 0 2
            if j == 3: #32 63
                print(x, j) # 62
                break
