def f(start, l):
    global s
    if l>10:
        return s
    elif l==10:
        s.add(start)
    else:
        s.add(f(start+5, l+1))
        s.add(f(start*2, l+1))
s=set()
print(f(10,0))