with open('17_4597.txt') as f:
    sp = [int(x) for x in f]
mn = min(sp)
maxx=k=0
for i in range(len(sp)-1):
    if sp[i]%117==mn or sp[i+1]%117==mn:
        k+=1
        maxx=max(maxx, sp[i]+sp[i+1])
print(k, maxx)


