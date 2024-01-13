l=0
for i in range(len(sp)):
    p*=sp[i]
    while p%m==0:
        p//=a[l]
        l+=1
    count+=(i-l)+1

