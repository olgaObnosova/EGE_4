with open('27-A_11468.txt') as f:
    n=int(f.readline())
    spa=[]
    spb=[]
    for i in range(n):
        spa.append(int(f.readline()))
    for i in range(n):
        spb.append(int(f.readline()))
minn=float('inf')
for i in range(n):
    for j in range(n):
        if abs(spa[i]-spb[j])<minn:
            minn=abs(spa[i]-spb[j])
print(minn)
print(int('31240', 5))