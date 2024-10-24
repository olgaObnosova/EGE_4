sp=[0]*100
sp[10]=10
for i in range(10, 100):
    if sp[i-3]!=0:
        sp[i] = sp[i - 3] + 3
    if i%3==0:
        sp[i]=sp[i//3]*3
print(sp)
sp=set(sp)

k=0
for x in sp:
    if x%2!=0:
        k+=1
print(k)

