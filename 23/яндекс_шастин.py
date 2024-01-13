def f(start, stop, k):
    if start>stop:
        return 0
    elif start==stop and (k[-1]=='A' or k[-1]=='B'):
        return 1
    elif start==stop and (not(k[-1]=='A' or k[-1]=='B')):
        return 0

    return f(start+2, stop, k+'A')+\
           f(start*2, stop, k+'C')+f(start+5, stop, k+'B')
print(f(8, 40, ''))
