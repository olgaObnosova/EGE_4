with open('24-9.txt') as f:
    f=f.readline()
gl='AEIOUY'
kg=0
if f[0] in gl:
    kg+=1
st=f[0]
maxl=0
for i in range(1, len(f)):
    if f[i] in gl:
        kg += 1
    if f[i-1]<f[i] and kg<2:
        st+=f[i]
        #print(st)
        maxl=max(maxl, len(st))
    else:
        st=f[i]
        if f[i] in gl:
            kg=1
        else:
            kg=0
print(maxl)

