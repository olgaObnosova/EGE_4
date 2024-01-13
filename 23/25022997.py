def f(start, stop):
    if start>stop or start==40:
        return 0
    elif start==stop:
        return 1
    return f(start+1, stop)+f(start*3, stop)+f(start*5, stop)
print(f(1,20)*f(20,100))
