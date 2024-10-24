import fnmatch as f
for i in range(1203450671094, 10**13, 206):
    if f.fnmatch(str(i), '12?345?67089?'):
        print(i, i//206)