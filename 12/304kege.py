a='>'+15*'1'+20*'2'+20*'3'
while '>1' in a or '>2' in a or '>3' in a:
    if '>1' in a:
        a=a.replace('>1','22>',1)
    if '>2' in a:
        a=a.replace('>2','2>1',1)
    if '>3' in a:
        a=a.replace('>3','1>',1)
s=0
for x in a:
    if x!='>':
        s+=int(x)
print(s)