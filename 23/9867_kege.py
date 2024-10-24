def f(st, e, k):
    if st>e and k[-3:]!='BAB':
        return 0
    elif st==e and k[-3:]=='BAB' :
        return 1
    return f(st+1, e,k+'A')+f(st*2, e,k+'B')\
           +f(st+5, e,k+'C')
print(f(5, 62, ''))