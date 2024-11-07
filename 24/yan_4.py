with open('24.txt') as f:
    f = f.readline()
z = '0123456789'
ch='02468'
k = 0
maxx = maxl=0
s=''
for i in range(len(f)):
    if f[i] in z:
        s += f[i]
    else:
        if len(s)>maxl:
            maxl=len(s)
            otv=s
        if len(s)!=0 and s[-1] in ch:
            maxx=max(int(s), maxx)
        elif len(s)!=0:
            while s[-1] not in ch:
                s=s[:-1]
                if len(s)==0:
                    break
            if len(s)!=0:
                maxx=max(int(s), maxx)

        s = ''
print(otv, maxx)