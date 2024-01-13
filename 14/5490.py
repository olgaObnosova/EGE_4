for x in '0123456789abcdefg':
    a = f'66{x}63'
    b = f'5{x}810'
    if (int(a, 17) - int(b, 17)) % 11 == 0:
        print(x, (int(a, 17) - int(b, 17)) // 11)
