a = open('27.txt').readlines()
k = int(a[0])
n = int(a[1])
m = 0
for i in range(len(a[2:])):
    z = 0
    for b in range(i, len(a[2:])):
        z += int(a[b])
        if b - i >= k:
            m = max(m, z)
print(m)