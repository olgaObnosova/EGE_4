def f(start, stop, k):
    if start > stop:
        return 0
    elif 'BB' in k:
        return 0
    elif start == stop and 'BB' not in k:
        return 1
    elif start == stop and 'BB' in k:
        return 0
    else:
        return f(start+2, stop, k+'A') + f(start**2, stop, k+'B')\
               + f(start*3, stop, k +'C')
print(f(2, 64, ''))