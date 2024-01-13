import fnmatch as f
for i in range(20, 100):
    ch = 2**i - 1
    if f.fnmatch(str(ch),'*8*3') and ch%9==0:
        s = 0
        for x in str(ch):
            s+=int(x)
        print(ch, s)
