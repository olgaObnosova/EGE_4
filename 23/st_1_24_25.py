def f(st, end):
    if st<end:
        return 0
    elif st==end:
        return 1
    return f(st-2, end)+f(st//2,end)+f(st//3,end)
print(f(40, 20)*f(20, 4))