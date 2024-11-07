for x in range(2030, 0, -1):
    k = 0
    a = 7**170 + 7**100 - x
    while a!=0:
        if a%7==0:
            k+=1
        a = a//7
    if k == 71:
        print(x)
        break



