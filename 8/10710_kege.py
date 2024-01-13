import itertools as it
n = list(it.product('ЕКМОПРТЬЮ', repeat=5))

for i in range(len(n)):
    x = ''.join(n[i])
    if (i+1)%2!=0 and x[0]!='Ь' and x.count('К')==2:
        print(i+1)
