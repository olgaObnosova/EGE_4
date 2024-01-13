def f(start, stop):
    if start > stop or start == 15: #избегание
        return 0
    elif start == stop:
        return 1
    else:
        return f(start+1, stop) + f(start+3, stop) \
               + f(start*2, stop)
print(f(1, 9) * f(9,27)) # обязательное посещение