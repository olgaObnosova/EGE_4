with open('24.txt') as f:
    f = f.readline()
maxl=-float('inf')
otv=''
f=f.replace('++', '@')
f=f.replace('+*', '@')
f=f.replace('*+', '@')
f=f.replace('**', '@')
f=f.split('@')
for x in f:
    x=x.replace('+', '@')
    x=x.replace('*', '@')
    x=x.split('@')
    k=0
    for y in x:
        if len(y)>0 and y[0]!='0':
            k+=1
            otv += y + ' '
            if k>maxl:
                maxl = max(maxl, k)
                otv2=otv
        else:
            k=0
            otv=''
print(maxl, otv2)