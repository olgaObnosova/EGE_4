def f(s, k):
    if k == 6:
        if 34<= s <= 59:
            rez.add(s)
        return
    return f(s + 1, k + 1), f(s + 2, k + 1), f(s * 2, k + 1)

rez =  set()
f(1, 0)
print(len(rez))