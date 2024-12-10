def f(st, end):
    if st>end:
        return 0
    elif st==end:
        return 1
    #msxc = max([int(x) for x in str(st)])
    return f(st+3,end) +\
           f(st+max([int(x) for x in str(st)]), end)
print(f(10, 24)*f(24,41))