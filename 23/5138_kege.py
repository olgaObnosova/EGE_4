def f(start, end):
    if start > end or start == 17:
        return 0
    elif start == end:
        return 1
    return f(start+1, end) + f(start * 2, end) \
           + f(start**2, end)
print(f(2, 16) * f(16,65))

