for x in range(150):
    a = 5*150**4+150**3+x*150**2+2*150+9
    b = x*150**3+2*150+3
    if (a+b)%149==0:
        print(x, (a+b)//149)