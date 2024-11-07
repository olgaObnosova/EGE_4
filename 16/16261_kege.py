f = '0123456789abcdefghijk'
for x in f:
    for y in f:
        t = int(f'943697{x}21', 21) - int(f'2{y}9253', 21)
        #if t==17394273143:
            #print(x, y)
        if t % 20 == 0:
            print(int(x,21) - int(y, 21), t // 20)