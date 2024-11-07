pr=[2,3,5,7,11,13,17,19,23,29,31,37,41,43]
sp=[0]*46
sp[14]=1
posli=0
for i in range(14,46):
    if i!=33:
        sp[i]+=sp[i-2]
        if i in pr:
            sp[i]+=sum(sp[posli:i])
            posli = i
print(sp)

