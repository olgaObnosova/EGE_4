for i in range(100):
    n=bin(i)[2:]
    n=n.replace('0','*')
    n=n.replace('1','0')
    n=n.replace('*','1')
    n=n+'1'
    if n.count('1')%2==1:
        n+='1'
    else:
        n+='0'
    if int(n,2)>180:
        print(i)
        break