maxx=0
print(bin(238)[2:], bin(51)[2:], bin(202)[2:])
for n in range(3, 10000):
    a='8'+n*'7'
    while '57' in a or '877' in a or '777' in a:
        if '57' in a:
            a=a.replace('57', '7', 1)
        if '877' in a:
            a=a.replace('877', '75', 1)
        if '777' in a:
            a=a.replace('777', '8', 1)
    k=1
    for x in a:
        k*=int(x)
    maxx=max(maxx, k)
print(maxx)