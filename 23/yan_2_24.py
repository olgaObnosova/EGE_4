def f(start, stop):
    if start > stop or start==81:
        return 0
    elif start == stop:
        return 1
    return f(start + start//10, stop) + \
            f(start+3, stop) + f(2*start-1, stop)
print(f(42,73) * f(73, 89))