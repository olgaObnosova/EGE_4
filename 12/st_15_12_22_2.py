from itertools import product
word = product('12', repeat=20)
maxx = 0
prov_maxx = 0
for i in word:
    a = ''.join(i)
    #print(a)
    a = '0' + a + '0'

    while '00' not in a:
        a = a.replace('012','30',1)
        if '011' in a:
            a = a.replace('011','20',1)
            a = a.replace('022','40',1)
        else:
            a = a.replace('01', '10',1)
            a = a.replace('02', '101',1)
    if a.count('1') == 6 and a.count('2') == 5:
        prov_maxx = a.count('4')
        maxx = max(prov_maxx,maxx)
print(maxx)