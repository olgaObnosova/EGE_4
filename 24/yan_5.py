with open('24-8.txt') as f:
    f=f.readline()
spT=[]
spU=[]
maxx=0
for i in range(len(f)):
    if f[i]=='T':
        spT.append(i)
    if f[i]=='U':
        spU.append(i)
for i in range(51,len(spU)):
    if abs(spU[i]-spU[i-51])>maxx:
        maxx=max(abs(spU[i]-spU[i-51]), maxx)
        otv=spU[i]
        otv2=spU[i-51]
print(maxx)
max2=0
sp2=[]
print(otv, otv2)
for i in range(len(spT)):
    #if spU[i]>662595:
        #print(spU[i])
    if spT[i]>1148656 and spT[i]<1149854:
        sp2.append(spT[i])
#print(sp2)
for i in range(101, len(sp2)):
    if abs(sp2[i]-sp2[i-101])>max2:
        max2=max(abs(sp2[i]-sp2[i-101]), max2)
        otv3=sp2[i]
        otv4=sp2[i-101]
print(max2, otv3, otv4)



