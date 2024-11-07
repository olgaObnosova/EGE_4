alf='qwertyuiopasdfghjklzxcvbnm'
s=''.join(sorted(alf))
print(s)
for x in '0123456789abcdefghijklmno':
    a=int(f'17{x}35', 27)
    b=int(f'{x}742m', 27)
    x = int(x, 27)
    if (a+b+(x*x*x))%23==0:
        print((a+b+(x*x*x))//23, x)