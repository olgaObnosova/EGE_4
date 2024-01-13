def tr(i):
    s=''
    while i>0:
        s+=str(i%3)
        i=i//3
    return s[::-1]
minn=999999999
for n in range(1,10000):
    r=tr(n)
    k=r.count('1')+r.count('2')*2
    if k%4==0:
        r='1'+r[:-2]
    else:
        ost=tr(k%4*3)
        r=r+ost
    r=int(r, 3)
    #print(r)
    if r>353:
        minn=min(minn, r)
print(minn)