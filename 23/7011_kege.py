def f(s, e, t):
    if s > e or s == 28 or 'baca' in t:
        return 0
    elif s == e and 'baca' not in t:
        return 1
    return f(s + 2, e, t + 'a') + f(s + 3, e, t + 'b')\
           + f(s * 2, e, t + 'c')
print(f(2,40,''))