
def f(st, ed, k):
    if st > ed or k.count('A')>2:
        return 0
    if st == ed:
        return 1
    else:
        return f(st - 2, ed, k + 'A') +\
               f(st * 2, ed, k + 'B') + \
               f(st * 3, ed, k + 'C')
print(f(6, 48, ''))