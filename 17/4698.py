with open('17-243.txt')as f:
    sp = []
    mx127 = -9999999
    for line in f:
        sp.append(int(line))
        if int(line)%127==0:
            mx127 = max(mx127,int(line))
print(mx127)
k = 0
mn = 999999999
for i in range(len(sp)-1):
    if (sp[i] > mx127 or sp[i+1] > mx127) \
            and ('31' in oct(sp[i]) \
                 or '31'in oct(sp[i])):
        k+=1
        mn = min(mn,sp[i]+sp[i+1])
print(k)
print(mn)