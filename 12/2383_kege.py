a = '>' + 11 * '1' + 12 * '2' + 30 * '3'
while '>1' in a or '>2' in a or '>3' in a:
    if '>1' in a:
        a=a.replace('>1','22>')
    if '>2' in a:
        a=a.replace('>2','222>')
    if '>3' in a:
        a=a.replace('>3','1>')
#print(a.count('1') + a.count('2') * 2)
s=0

for x in a:
    if x!='>':
        s+=int(x)
print(s)