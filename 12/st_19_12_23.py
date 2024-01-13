for i in range(10):
    for j in range(10):
        for k in range(10):
            a='0'+i*'1'+j*'2'+k*'3'+'0'
            while '00'not in a:
                a=a.replace('01','220',1)
                a = a.replace('02', '1013', 1)
                a = a.replace('03', '120', 1)
            if a.count('1')==13 and a.count('2')==18:
                print(i+j+k+2)
