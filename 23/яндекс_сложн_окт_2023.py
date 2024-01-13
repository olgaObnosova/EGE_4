def f(start, stop,k):
    if start>stop or start==27 or k==16:
        return 0
    elif start==stop:
        return 1
    else:
        return f(start+2, stop, k+1)+\
               f(start*3, stop, k+1)+f(start**3, stop, k+1)
print(f(3, 125, 0))