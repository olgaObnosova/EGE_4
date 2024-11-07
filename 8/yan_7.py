import itertools as f
s=list(f.product('ВОЗДУХ', repeat=5))
k=0
for x in s:
    x=''.join(x)
    if (x.count('О') + x.count('У') == 1)  and \
        (('ВО' not in x and 'ОВ' not in x) \
         and ('ОХ' not in x and 'ХО' not in x)\
        and ('ВУ' not in x and 'УВ' not in x)\
        and ('УХ' not in x and 'ХУ' not in x)):
        k+=1
print(k, x)