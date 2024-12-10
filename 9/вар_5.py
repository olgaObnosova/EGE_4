with open('9_5.txt') as f:
    f = [[int(x) for x in line.split()] for line in f]
k=0
for x in f:
    snep=0
    ppov=1
    if len(set(x))!=len(x):
        for ch in x:
            if x.count(ch)==1:
                snep+=ch
            else:
                ppov*=ch
        if 3*snep<=ppov:
            k+=1
print(k)


