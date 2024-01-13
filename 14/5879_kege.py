for x in range(15):
    a = 3*15**4+ x*15**3+15**2+5*15+x
    b=int(f'3{x}51')**2 + 2*int(f'3{x}51')+3
    c=x**x
    d = int(f'1{x}3')**2+x*int(f'1{x}3') +3
    e = (x+1)**2+x*(x+1)+2
    if (a+b+c+d+e)%13==0:
        print(x)
        otv=a+b+c+d+e
        print(otv)
while otv!=0:
    print(otv%13, end = ' ')
    otv=otv//13