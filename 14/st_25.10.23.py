maxx=0
for x in range(37):
    for y in range(37):
        a = 1*37**7+2*37**6+x*37**5+6*37**4+4*37**3+3*37**2+\
            y*37+7
        if a%36==0:
            s = y*37+x
            maxx = max(maxx, s)
print(maxx)


