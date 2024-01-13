def f(s, e, p=0):
    if s == e: return 1
    if s > e: return 0
    if p== 1:
        return  f(s*2, e, 2) + f(s +3, e, 3)
    if p==2:
        return f(s + 1, e, 1) + f(s +3, e, 3)
    if p==3:
        return f(s + 1, e, 1) + f(s *2, e, 3)
    return f(s+1,e,1)+f(s + 2, e, 2) + f(s * 2, e, 3)

print(f(5001, 10000, 0))