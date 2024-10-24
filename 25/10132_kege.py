import fnmatch as f
for i in range(30502140, 10**9):
    if i%1024==0:
        print(i)
        break
for i in range(30502912, 10**9,1024):
    if f.fnmatch(str(i),'3?5?21*4?'):
        print(i, i//1024)