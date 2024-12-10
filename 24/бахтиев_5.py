with open('24-2.txt') as f:
    f=f.readline()
st=''
sp=[]
i=0
while i<len(f):
    if f[i]=='L':
        st=i
        if f[i]=='E':
            end=i
            if 'O' in f[st:end] and 'V' in f[st:end]:
                sp.append(f[st:end+1])
            st=i
        i+=1
print(sp[:5])

