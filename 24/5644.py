from fnmatch import *

kmax = 0
a = open("24-228.txt").readline()

a = a.split("XX")

for j in a:
    if fnmatch(str(j), "3????78??45"):
        kmax = max(int(j), kmax)

a1 = 0
a2 = 1
for l in str(kmax):
    if int(l) % 2 ==0:
        a2 = a2 * int(l)
    else:
        a1 = a1 + int(l)
print(a2 + a1)
