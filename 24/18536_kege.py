with open('24_18536.txt') as f:
    f=f.readline()
f=f.replace('--', '@')
f=f.replace('**', '@')
f=f.replace('*-', '@')
f=f.replace('-*', '@')
f=f.split('@')
sp=[]
mx=k=0
zn='-*'
otv=''
for x in f:
    k=0
    st=''
    for i in range(len(x)-1): #2-03*5*00
        if not(x[i] in zn and x[i+1]=='0' and x[i+2] not in zn):
            k+=1
            st+=x[i]
            if eval(st)==0:
                if k>mx:
                    mx=k
                    otv=st
        else:
            k=0
            st=''
    #sp.append((len(x), x))
#sp.sort(reverse=True)
print(mx)
print(otv)
#print(sp[1])


