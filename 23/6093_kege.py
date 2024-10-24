def f(st, ed, k):
    if st > ed or k > 3:
        return 0
    elif st == ed:
        return 1
    else:
        return f(st + 1, ed, k + 1) + f(st + 2, ed, k + 1)\
               + f(st * 3, ed, k + 1)
count = 0
for i in range(4, 400, 2):
    d = f(4, i, 0)
    if d:
        print(d, i)
        count+= d
print(count)