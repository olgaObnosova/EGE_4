def f(st, end, k):
    if st > end:
        return 0
    elif st==end and k[-1]!='C':
        return 1
    return f(st+2, end, k+'A') + f(st+5, end, k+'B')+ \
           f(st**2, end, k + 'C')
print(f(4, 36, ' '))