sp = [0]*30
sp[2] = 1
for i in range(3,15):
    if i%2==0:
        sp[i]=sp[i-1]+sp[i//2]
    else:
        sp[i]=sp[i-1]
for i in range(15, 28):
    if i!=25:
        sp[i]=sp[i-1]
sp[28]=sp[27]+sp[14]
sp[29]=sp[28]
print(sp[29])
s='dfaaaawgrhe'
print(s.count('a',5))
    
    
