def f(start, stop, sl, ym):
    if start > stop:
        return 0
    elif start == stop and ym > sl:
        return 1
    elif start == stop and ym <= sl:
        return 0
    else:
        return f(start+3,stop, sl+1) +f(start*2,stop,ym+1)+f(start*7, stop, ym+1)
    print(f(2,472,0,0))
