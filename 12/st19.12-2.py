maxx=0
for i in range(20):
    for j in range(20):
        for k in range(20):
            a='0'+i*'1'+j*'2'+k*'3'+'0'
            for i in range(50):
            if a.count('1')==13 and a.count('2')==18:
                maxx=max(maxx, i+j+k+2)
print(maxx)