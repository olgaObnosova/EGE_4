sp=[0]*681
sp[2]=1
for i in range(3):
    if i**0.5==int(i**0.5):
        sp[i]+=sp[int(i**0.5)]
    sp[i]+=sp[68-i%68]
    sp[i]+=sp[i%10]
print(sp[680])