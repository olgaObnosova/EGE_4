with open('5644.txt') as f:
    f = f.readline().split('XX')
    maxx=0
    for x in f:
        if len(x)==11 and x[0]='3' ans x[5]+x[6]=='78'\
                                and x[9:]='45' and x.isdigit():
            maxx=max(maxx, int(x))
print(maxx)
maxx=str(maxx)
s=0
p=1
for i in maxx:
    if int(i)%2!=0:
        s+=int(i)
    else:
        p*=int(i)
print(s+p)
