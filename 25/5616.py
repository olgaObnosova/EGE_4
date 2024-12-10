import fnmatch as f
for i in range(9797, 10**7+1, 9797):
    if f.fnmatch(str(i), '3*1'):
        print(i, i//9797)