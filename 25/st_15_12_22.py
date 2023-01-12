from fnmatch import fnmatch

for i in range(1000000, 10 ** 9):
    if fnmatch(str(i), '12*63?5?'):
        if i % 3123 == 0:
            print(i)
