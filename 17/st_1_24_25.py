with open('17.txt') as f:
    sp=[int(x) for x in f]
minn=min(sp)
maxx=max(sp)
k=maxs=0
for i in range(len(sp)-1):
    if (sp[i]%3==minn%3 or sp[i+1]%3==minn%3) and \
            (sp[i] % 7 == maxx % 7 or sp[i + 1] % 7 == maxx % 7):
        k+=1
        maxs=max(maxs, sp[i]+sp[i+1])
print(k, maxs)
