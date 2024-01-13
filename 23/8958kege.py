def f(start, stop):
    if start< stop or start==22:
        return 0
    elif start==stop:
        return 1
    return f(start-2,stop)+f(start//2,stop)+f(start//3,stop)
print(f(40,2))