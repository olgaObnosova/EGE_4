import itertools as f
s=list(f.product('ГЕКЭ023', repeat=4))
k=0
for x in s:
    x=''.join(x)
    k+=1
    if (x[0]=='2'or x[0]=='0' or x[0]=='3') and x[0]!=x[1] and x[1]!=x[2] and x[2]!=x[3]:
        print(k, x)
        break