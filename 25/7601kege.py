import fnmatch as f
for i in range(1200361,10**8):
    if i%273==0 and f.fnmatch(str(i),'12??36*1'):
        print(i, i//273)
