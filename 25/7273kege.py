import fnmatch as f

for i in range(123450798, 10**9,23):
    if f.fnmatch(str(i),'12345?7?8') and i%23==0:
        print(i, i//23)