with open('17_17530.txt') as f:
    sp=[int(x) for x in f]
minn=min(sp)
k=0
mins=99999999
for i in range(len(sp)-1):
    if sp[i]%55==minn or sp[i+1]%55==minn:
        k+=1
        mins=min(mins, sp[i]+sp[i+1])
print(k)
print(mins)