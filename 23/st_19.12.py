def f(start, stop, k):
    if start > stop:
        return 0
    elif start==stop and 'AA' not in k:
        return 1
    elif 'AA' in k:
        return 0

    return f(start-1, stop, k+'A')+f(start*2, stop, k+'B')\
           +f(start*3, stop, k+'C')
print(f(3, 20, ''))