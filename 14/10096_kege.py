for x in range(19):
    a=9*19**7+8*19**6+8*19**5+9*19**4+7*19**3+x*19**2+2*19+1
    b=2*19**4+x*19**3+9*19**2+2*19+3
    if (a+b)%18==0:
        print((a+b)//18)