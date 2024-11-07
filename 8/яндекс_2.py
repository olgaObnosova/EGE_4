import itertools as t
sp=list(t.product('гипербола', repeat = 6))
gl = 'иеоа'
sogl = 'гпрбл'
k=0
for x in sp:
    x=''.join(x)
    if x[0] not in gl and x[-1] not in gl:
        x=x.replace('г', '*')
        x = x.replace('п', '*')
        x = x.replace('р', '*')
        x = x.replace('б', '*')
        x = x.replace('л', '*')
        x = x.replace('и', '&')
        x = x.replace('е', '&')
        x = x.replace('о', '&')
        x = x.replace('а', '&')
        if '*&*' not in x:
            k+=1
print(k)


