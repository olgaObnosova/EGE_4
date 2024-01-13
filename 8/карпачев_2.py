import itertools as f
s=list(f.product('АЕИКМНХ', repeat=7))
k=0
fl1=0
fl2=1
for x in s:
    x=''.join(x)
    if x=='АНИМЕКХ':
        fl1=1
    if x=='МЕХАНИК':
        fl2=0
        break
    if fl1 and fl2:
        x=x.replace('К', '*')
        x=x.replace('Н', '*')
        x=x.replace('Х', '*')
        if x.count('М')>=1 and x.count('М*')==0 \
                and x.count('*М')==0 \
                and 'ММ' not in x:
            k+=1
print(k-1)