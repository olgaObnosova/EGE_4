
for x in range(1, 1000):
    for y in range(1, 1000):
        k=0
        a=5**50+5**30-5**x-y-5**y-x
        if a>0:
            while a!=0:
                if a%5==0:
                    k+=1
                a=a//5
            if k==10:
                print(x * y)