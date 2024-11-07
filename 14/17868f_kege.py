alf = '0123456789abcdefghi'
for x in alf:
    a = int(f'98897{x}21', 19) + int(f'2{x}923', 19)
    if a%18==0:
        print(a//18, x)
