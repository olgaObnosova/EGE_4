with open('4919.txt') as f:
    k = 0
    f = f.readline()
    while f :
        na = f.find('A')
        nb = f.find('B')
        if na < nb and len(f[na:nb+1])>19 and f[na:nb+1][0]=='A'\
           and f[na:nb+1].count('F')==2 and f[na:nb+1].count('A')==1:
            k+=1
            f = f[nb:]
        elif na>nb:
            f = f[nb+1:]
        elif na<nb:
            f = f[na+1:]
        if f.count('A')==0 or f.count('B')==0:
            break
print(k)
        
