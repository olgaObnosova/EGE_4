
for i in range(200):
    a=8**150+4**120-i
    a=oct(a)[2:]
    if a[-4:]=='7531':
        print(i)
print(1030%7)