k=0
for i in range(1,1000):
    a=i*'1'
    while '111' in a:
        a=a.replace('111','2',1)
        a = a.replace('222', '11',1)
        a = a.replace('1', '2',1)
    if '1'  not in a:
        print(i)
        k+=1

print(*[bin(int(i))[2:] for i in '121.96.174.205'.split('.')])
print(2023*2022)