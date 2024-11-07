import itertools as t
comb= set(t.permutations('КИДАЛА',r=5))
k=0
for x in comb:
    x=''.join(x)
    if 'АА' not in x and 'КК' not in x and 'ДД' not in x and \
            'ЛЛ' not in x and 'ИИ' not in x:
        k+=1
print(k)
