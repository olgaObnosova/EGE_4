def f(start, stop,k):
    if start>stop:
        return 0
    elif start==stop and 'CAC' in k:
        return 1
    elif start==stop and 'CAC' not in k:
        return 0
    return f(start+1, stop, k+'A')+\
               f(start*3, stop, k+'B')\
           +f(start+5, stop, k+'C')
print(f(3, 20, ''))