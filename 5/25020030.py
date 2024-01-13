for i in range(1000, 100,-1):
    for j in range(100, 1000):
        sot = i//100+j//100
        des = i//10%10+j//10%10
        ed= i%10+j%10
        zap =str(ed)+str(sot)+str(des)
        kontr=zap[-4:-1]
        #print(zap, kontr)
        if int(kontr)==2:
            print(i, j)
