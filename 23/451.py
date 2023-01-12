def f(start, stop):
    if start > stop or start == 12:
        return 0
    elif start == stop:
        return 1
    else:
        return f(start + 1, stop) + f(start + 3, stop)


print(f(5, 15) * f(15, 25))
