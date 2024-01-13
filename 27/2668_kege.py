sp=[]
min1 = float('inf')
minpr = float('inf')
for i in range(len(sp)):
    min1 = min(min1, sp[i])
    minpr = min(minpr, min1**2 + sp[i+5]**2)
print(minpr)

