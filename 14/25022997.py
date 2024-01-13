for x in '0123456789abcdefghi':
    a=int(f'a3{x}74',19)
    b=int(f'{x}40846',19)
    if (a+b)%9==0:
        print(x,(a+b)//9)