alf=list('qwertyuiopasdfghjklzxcvbnm')
alf.sort()
alf=''.join(alf)
print(alf[:17])
for x in '0123456789abcdefghijklmnopq':
    a=int(f'123{x}24',27)
    b=int(f'135{x}78', 27)
    if (a+b)%26==0:
        print(x, (a+b)//26)