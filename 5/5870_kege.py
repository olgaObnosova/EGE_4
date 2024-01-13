import math

minn = float('inf')
for i in range(64, 1000):
    n = bin(i)[2:]
    if n.count('1') % 2 == 0:
        n1 = n[:-4]
        n2 = n[-4:]
        n2 = n2.replace('1', '2')
        n2 = n2.replace('0', '1')
        n2 = n2.replace('2', '0')
        n = n1 + n2
    else:
        n1 = n[:-5]
        n2 = n[-5:-1]
        n3 = n[-1]
        n2 = n2.replace('1', '2')
        n2 = n2.replace('0', '1')
        n2 = n2.replace('2', '0')
        # print(n1)
        # print(n2)
        # print(n3)
        n = n1 + n2 + n3
        # print(n)
        # break
    if int(n, 2) < minn:
        minn = int(n, 2)
        otv = i
print(otv)
print(math.log2(180*3600))
print(math.log2(123*365.25*24*60*60))
print(240*10**9/8*10)
print((14**4*3+15**2+75+3+2+3)%13)