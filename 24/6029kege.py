with open('24_6029.txt') as f:
    f=f.readline().strip()
f=f.split('D')
mx=0
for x in f:
    x=x.replace('EF','**')
    x = x.replace('FE', '&&')
    if '*' not in x and 'F' not in x and 'F' not in x:
        mx=max(mx, len(x))
    if '&' not in x and 'F' not in x and 'F' not in x:
        mx=max(mx, len(x))
print(mx)