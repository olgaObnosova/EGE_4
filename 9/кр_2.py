f=open('9.txt')
k=0
r=[]
for s in f:
    a=[int(x) for x in s.split()]
    a3=[x for x in a if a.count(x)>2]
    anch=[x for x in a if x%2!=0]
    if (len(a3)==0) and len(anch)>1 and len(anch)%2!=0:
            k+=1
    print(a, a3, anch, k)
print(k)