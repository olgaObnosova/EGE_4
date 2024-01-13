import itertools as t
l=set(t.permutations('ВИКТОРИЯ',8))
k=0
for x in l:
    x=''.join(x)
    if 'ИОИ' not in x and \
            not(x.find('И')<x.find('О')<x.rfind('И')):
        k+=1
print(k)


