maxx=0
for i in range(204):
    a='1'*i+'2'+'1'*(203-i) #'1'*197 +'2'+'1'*6
    while '111' in a or '222' in a:
        if '111' in a:
            a=a.replace('111', '22', 1)
        else:
            a=a.replace('222', '11', 1)
    if len(a)>maxx:
        r=i
        maxx=len(a)
        ot=a
print(maxx, r)
print(ot)