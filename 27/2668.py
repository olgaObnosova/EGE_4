with open('2668') as f:
    n = int(f.readline())
    sp = [int(x) for x in f]
min1=float('inf')
mins=float('inf')
for i in range(len(sp)-5):
    min1=min(min1, sp[i])
    mins = min(mins, min1**2 +sp[i+5]**2)
print(mins)

