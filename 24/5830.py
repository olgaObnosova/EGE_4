with open('5830.txt') as f:
    f = f.readline()
    kx=kotv=0
    s = f[0]
    otv=''
    for i in range(1,len(f)):
        if f[i]!=f[i-1]:
            s+=f[i]
            if len(s)>= len(otv):
                otv = s
        else:
            s = f[i]
otv_1 = set(otv)
for x in otv_1:
    #print(otv.count(x))
    if otv.count(x)> kx:
        kx = otv.count(x)
        g=x
        
print(otv)
print(kx)
