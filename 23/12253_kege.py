def f(start, end):
    if start > end or start ==16:# не содержало это число
        return 0
    elif start == end:
        return 1
    return f(start+1,end) + f(start + 3, end) \
        + f(start**2, end)
print(f(3, 20) * f(20, 26)) # обязательное к посещению