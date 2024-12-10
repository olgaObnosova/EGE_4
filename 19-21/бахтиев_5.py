def f(a, h, ph):
    if a>=313:
        return h%2 == ph%2
    elif h == ph:
        return False
    comb=[f(a+2, h+1, ph), f(a+3, h+1, ph), f(a*3, h+1, ph)]
    return any(comb) if (h+1)%2==ph%2 else all(comb)
for x in range(1, 313):
    #print(x, f(x, 0, 2))
    if f(x, 0, 4) and not(f(x, 0, 2)):
        print(x)
