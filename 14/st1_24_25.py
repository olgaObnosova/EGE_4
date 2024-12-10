alf=sorted('qwertyuiopasdfghjklzxcvbnm')
alf=''.join(alf)
alf='0123456789'+alf
for x in alf:
    a=int(f'f29{x}8ead6', 36)
    b=int(f'ba{x}de0c1b', 36)
    if (a*b)%36==0:
        print(x)