with open('17_remez.txt') as f:
    sp=[int(x) for x in f]
cnt=0
minn=99999999
otv=[]
for i in range(len(sp)-9):
    k1 = k2 = k = 0
    if abs(sp[i])%3==1:
        k1+=1
    elif abs(sp[i])%3==2:
        k2+=1
    if sp[i]>7000:
        k+=1
    if abs(sp[i+1]) % 3 == 1:
        k1 += 1
    elif abs(sp[i+1]) % 3 == 2:
        k2 += 1
    if sp[i+1] > 7000:
        k += 1
    if abs(sp[i+2]) % 3 == 1:
        k1 += 1
    elif abs(sp[i+2]) % 3 == 2:
        k2 += 1
    if sp[i+2] > 7000:
        k += 1
    if abs(sp[i+3]) % 3 == 1:
        k1 += 1
    elif abs(sp[i+3]) % 3 == 2:
        k2 += 1
    if sp[i+3] > 7000:
        k += 1
    if abs(sp[i+4]) % 3 == 1:
        k1 += 1
    elif abs(sp[i+4]) % 3 == 2:
        k2 += 1
    if sp[i+4] > 7000:
        k += 1
    if abs(sp[i+5]) % 3 == 1:
        k1 += 1
    elif abs(sp[i+5]) % 3 == 2:
        k2 += 1
    if sp[i+5] > 7000:
        k += 1
    if abs(sp[i+6]) % 3 == 1:
        k1 += 1
    elif abs(sp[i+6]) % 3 == 2:
        k2 += 1
    if sp[i+6] > 7000:
        k += 1
    if abs(sp[i+7]) % 3 == 1:
        k1 += 1
    elif abs(sp[i+7]) % 3 == 2:
        k2 += 1
    if sp[i+7] > 7000:
        k += 1
    if abs(sp[i+8]) % 3 == 1:
        k1 += 1
    elif abs(sp[i+8]) % 3 == 2:
        k2 += 1
    if sp[i+8] > 7000:
        k += 1
    if abs(sp[i+9]) % 3 == 1:
        k1 += 1
    elif abs(sp[i+9]) % 3 == 2:
        k2 += 1
    if sp[i+9] > 7000:
        k += 1
    if k1==k2 and k==5:
        cnt+=1
        otv.append(sum(sp[i:i+10]))
        minn=min(minn, sum(sp[i:i+10]))
print(cnt, minn, otv)

