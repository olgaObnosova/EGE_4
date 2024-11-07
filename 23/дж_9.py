def f(start, stop, k):
    if start>stop or k>2:
        return 0
    elif start==stop and k<=2:
        return 1
    else:
        return f(start + 2, stop, k+start % 2) +\
               f(start * 2, stop, k+start % 2)
print(f(3, 20,0)*f(20, 68, 0))