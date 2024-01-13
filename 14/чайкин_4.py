
maxx=0
for x in range(10, 14):
    for y in range(9, 14):
        a= 7*14**4+x*14**3+3*14**2+7*14+y
        b=9*x**3+y*x**2+6*x+3
        c=y**4+5*y**3+y**2+4*y+8
        if a+b-c>maxx:
            maxx=a+b-c
            x1=x
            y1=y
print(maxx/(x1+y1))
