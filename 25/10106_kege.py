import fnmatch as f
for i in range(1021574, 10**10):
    if i%2024==0:
        print(i)
        break
for i in range(1022120, 10**10, 2024):
    if f.fnmatch(str(i),'1?2157*4'):
        print(i, i//2024)