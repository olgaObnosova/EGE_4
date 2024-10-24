with open('24-dg6.txt') as f:
    f=f.readline().split('F')
maxl=0
for x in f:
    if x.count('A')==len(x):
        maxl=max(maxl, len(x))
    if x.count('B')==len(x):
        maxl=max(maxl, len(x))
    if x.count('C')==len(x):
        maxl=max(maxl, len(x))
    if x.count('D')==len(x):
        maxl=max(maxl, len(x))
    if x.count('E')==len(x):
        maxl=max(maxl, len(x))

print(maxl)
