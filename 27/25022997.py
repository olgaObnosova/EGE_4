with open('27_B_25022997.txt') as f:
    n=int(f.readline())
    k=int(f.readline())
    sp=[int(x) for x in f]
count=0
for i in range(len(sp)):
    for j in range(i+1, len(sp)):
        if (sp[i]+sp[j])%8==0 and abs(i-j)<=k:
            #print(sp[i],sp[j])
            count+=1
print(count)