ss='0123456789abcdefghijklmnopqrstuvwxyz'
for p in range(5,37):
    for x in ss[:p]:
        for y in ss[:p]:
            if int('12',p)*int('34',p)==int(x+y+'2',p):
                print(x,y,p)
print(int('54',6))