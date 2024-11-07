a='1'+105*'0'
while '10' in a:
    if '100' in a:
        a=a.replace('100', '1011')
    else:
        a=a.replace('10', '11')
a=int(a,2)
a=hex(a)[2:]
s=0
for x in a:
    s+=int(x, 16)
print(s)