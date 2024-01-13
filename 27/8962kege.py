with open('27_A_8962.txt') as f:
    k=int(f.readline())
    n = int(f.readline())
    sp=[int(x) for x in f]
maxx=0
print(k, sp[:1])
for i in range(len(sp)-1):
    for j in range(i+k, len(sp)):
        if i!=0 and (sp[i]+sp[j])>maxx and sp[i]>max(sp[:i])\
            and sp[j]>max(sp[:j]):
            maxx=sp[i]+sp[j]
        elif (sp[i]+sp[j])>maxx \
            and sp[j]>max(sp[:j]):
            maxx=sp[i]+sp[j]
print(maxx)
