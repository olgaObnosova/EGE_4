alf = '0123456789ab'
k = 0
for x1 in alf:
    for x2 in alf:
        for x3 in alf:
            for x4 in alf:
                for x5 in alf:
                    a = x1+x2+x3+x4+x5
                    if a[0]!='0' and a.count('7')==1 and \
                        a.count('9') + a.count('a') +a.count('b')<=3:
                        k+=1
print(k)

print('1111'.count('111'))


