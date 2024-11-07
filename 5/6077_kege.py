def f(n):
    n1 = n // 100
    n2 = n % 100 // 10
    n3 = n % 10
    return n1, n2, n3


for i in range(100, 1000):
    for j in range(100, 1000):
        i1, i2, i3 = f(i)
        j1, j2, j3 = f(j)
        s = str(i3 + j3) + str(i1 + j1) + str(i2 + j2)
        #print(s, s[-4:-1])
        s1 = s[-4:-1]

        if s1 == '02':
            print(i, j, s, s1 )
