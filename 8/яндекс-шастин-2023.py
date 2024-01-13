import itertools as f
s=list(f.product('ДЛМОУЬ', repeat=6))
k=0
counter=0
for x in s:
    k+=1
    x=''.join(x)
    if x[0]=='М':

        counter+=1
print(counter)
print(15553+7776)#7773 #15553