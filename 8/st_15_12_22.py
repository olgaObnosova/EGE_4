from itertools import product

k = 0
a = list(product('ВЕРОНИКА', repeat=6))
for x in a:
    x=''.join(x)
    if x.count('А') + x.count('Е') + x.count('О') + x.count('И') > x.count('В') + x.count('Р') + x.count('Н') + x.count(
        'К'):
        k += 1
print(k)
