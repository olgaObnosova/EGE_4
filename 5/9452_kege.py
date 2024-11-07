for i in range(1, 500):
    s=''
    n = bin(i)[2:]
    if i%2==0: #1001
        for x in n:
            s+=x*2#11000011
    else:
        n=n.replace('0','*')#1**1
        n=n.replace('1','0')#0**0
        n=n.replace('*','1')#0110
        s=n
    r=int(s, 2)
    if r>60:
        print(i)
        break



