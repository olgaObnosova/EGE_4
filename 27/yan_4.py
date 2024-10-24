with open('pr') as f:
    n=f.readline().strip()
k=1
for i in range(len(n)-1):
    if 0<int(n[i])<3 and int(n[i+1])>0:
        k=k*2
    elif int(n[i])==3 and int(n[i+1])<5:
        k*=2
    print(k, n[i])
print(k)

