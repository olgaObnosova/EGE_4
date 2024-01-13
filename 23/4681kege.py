def f(start, stop):
    if start > stop or start == 15:
        return 0
    elif start == stop:
        return 1
    return f(start+3, stop) + f(start*2, stop)
print(f(3, 27)*f(27, 63))
