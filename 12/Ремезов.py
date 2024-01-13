maxx=0
print(int('11111100',2))
for n1 in range(3, 150):
    for n2 in range(5, 56):
        a='0'*n1+'>'+'1'*n2
        while '00' in a or '11' in a or '0>' in a:
            if '00' in a:
                a=a.replace('00', '10', 1)
            if '11' in a:
                a=a.replace('11', '01', 1)
            if '0>' in a:
                a=a.replace('0>', '11>00', 1)
        sum=a.count('1')
        maxx=max(maxx, sum)

print(maxx)