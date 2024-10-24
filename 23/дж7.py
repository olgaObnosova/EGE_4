sp=[0]*63
sp[21]=1
for i in range(21,63):
    #i=21
    if i%10!=0:
        j=i+i%10
        if j<63:
            sp[j]+=sp[i]
    j=2*i
    if j<63:
        sp[j]+=sp[i]
    a1=i//10
    a2=i%10
    if a1!=a2:
        j=i+max(a1,a2)-min(a1,a2)
        if j<63:
            sp[j]+=sp[i]
print(sp)

