def f(st, end, k):
    if st>end or k>15:
        return 0
    elif st==end and k==15:
        return 1
    return f(st+sum([int(x) for x in str(st)]), end, k+1)+\
        f(int(str(st)[-1]+str(st)[:-1]), end, k+1)
s=set() #30+9+14+16+9+15+18+19+21+6
for i in range(1, 5100):
    d=f(15,i,0)
    if d:
        s.add(i)
print(len(s))