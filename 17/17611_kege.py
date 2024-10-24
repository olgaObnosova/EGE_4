with open('17_17611.txt') as f:
    sp = [int(x) for x in f]
max_7=-float('inf')
k=0
max_s=-float('inf')
for x in sp:
    if len(str(abs(x)))==4 and abs(x)%10==7:
        max_7=max(max_7, x)
for i in range(len(sp)-2):
    l=0
    if len(str(abs(sp[i]))) == 4 and abs(sp[i]) % 10 == 7:
        l+=1
    if len(str(abs(sp[i+1]))) == 4 and abs(sp[i+1]) % 10 == 7:
        l+=1
    if len(str(abs(sp[i+2]))) == 4 and abs(sp[i+2]) % 10 == 7:
        l += 1
    if l>=2 and sp[i]+sp[i+1]+sp[i+2]>max_7:
        k+=1
        max_s=max(max_s, sp[i]+sp[i+1]+sp[i+2])
print(k)
print(max_s)


