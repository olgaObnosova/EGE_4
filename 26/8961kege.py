with open('26_8961.txt') as f:
    sp=[]
    k,m,n=map(int,f.readline().split())
    for x in f:
        sp.append(int(x))
sp.sort(reverse=True)
stad = [m]*k
count=0
for x in sp:
    for i in range(len(stad)):
        if x<stad[i]:
            stad[i]=stad[i]-x
            count+=1
            break
print(count, sum(stad))





