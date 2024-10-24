import fnmatch as f
for i in range(2100069262, 10**10, 1777):
    if len(str(i))==10 and f.fnmatch(str(i),'21*68?79'):
        print(i, i//1777)