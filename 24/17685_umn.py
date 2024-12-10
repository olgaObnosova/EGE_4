with open('24_17685.txt') as f:
    f=f.readline()
f=f.replace('++', '@')
f=f.replace('**', '@')
f=f.replace('+*', '@')
f=f.replace('*+', '@')
sp=f.split('@')
sp.sort(key=len, reverse=True)
maxx=0
for x in sp[:5]:
    for i in range(len(x)):
        s=''
        for j in range(i, len(x)):
            s+=x[j]
            try:
                if eval(s)==0:
                    if len(s)>maxx:
                        maxx=max(maxx, len(s))
                        otv=s
            except:
                pass
print(maxx)
print(otv)