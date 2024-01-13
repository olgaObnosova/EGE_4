def f(start, stop, k):
    if start>stop:
        return 0
    elif 'AA' in k or 'BB' in k:
         return 0
    elif start==stop:
        return 1
    else:
        return f(start+1.5, stop, k+'A')+f(start+2.5, stop, k+'B')
otv=1
for i in range(100, 300-4+1, 4):
    st = i
    end = i+4
    otv*=f(i, i + 4, '')
    print(otv)
