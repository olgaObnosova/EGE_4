with open('24_15_12_22.txt') as f:
    f = f.readline()
f = f.split('F')
maxx = 0
for x in f:
    if x.count('A') <= 2:
        maxx = max(maxx, len(x))
print(maxx)
