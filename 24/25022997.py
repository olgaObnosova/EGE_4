with open('24.txt') as f:
    f=f.readline()
f=f.replace('SOLO','*')
f=f.split('*')
maxx=0
for i in range(len(f)):
    a=''.join(f[i:i+5])
    if int('0' in a)+int('1' in a)+int('2' in a)+ \
            int('3' in a) +int('4' in a)+ \
            int('5' in a) +int('6' in a)+ \
            int('7' in a) +int('8' in a)+\
            int('9' in a)>=5:
        if len(a)>maxx:
            maxx=len(a)
            b=f[i:i+5]
print(maxx, len('SOLO'.join(b)))
