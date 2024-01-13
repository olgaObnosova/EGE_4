m = 0
n = '123456789ABCDEFGHIJKLMNOPQRSTUV'

for x in '123456789ABCDEFGHIJKLMNOPQRSTUV':
    a = int(f'72{x}', 32)
    b = int(f'1C{x}7', 32)
    c = n.index(x)+1
    if (a + b + c**5) % c == 0:
        m = max(m, c)
print((a+b+c)/m)