with open ('24_yan_2.txt') as f:
    f=f.readline()
    f=f.split('A')
k=0
maxx=0
fl=0
sp=''
for x in f:
    if 'B' in x and fl==0:
        sp+=x
        fl+=1
        k+=len(x)+1
        if k > maxx:
            maxx=k
            otv=sp
    elif 'B' not in x and fl==1:
        k+=1 + len(x)
        sp+='A'+x
        if k > maxx:
            maxx=k
            otv=sp
    elif 'B' in x and fl==1:
        for i in x:
            if i!='B':
                k+=1
                sp+=i
                if maxx < k:
                    maxx = k
                    otv = sp
            sp=''
            k=0
            fl=0
print(maxx)
print(otv)
