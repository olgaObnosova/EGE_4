k=0
with open('5830.txt') as f:
    f = f.readline()
    s = set(f)
    for x in s:
        f = f.replace(x*2,'*')
    f = f.split('*')
    f = max(f, key = len)
s = set(f)
for x in s:
    if f.count(x)>k:
        k=f.count(x)
print(k)
