with open('26_11243.txt') as f:
    k, n = map(int, f.readline().split())
    sp = []
    for x in f:
        a, b = map(int, x.split())
        sp.append((a, b))
sp.sort()
r = [0] * k
cnt = cnt2 = cnt3 = 0
for x in sp:
    st, vr = x
    if st + vr + 2 < 1440:
        for i in range(k):
            if r[i] <= st:
                r[i] = st+vr+2
                cnt+=1
                otv = st +vr + 2
                break
            else:
                r.sort()
                r[0]= st +vr + 2
                cnt += 1
                cnt3+=1
                break
    else:
        cnt2+= 1

print(cnt, cnt2,cnt3,  n)
print(n - cnt - cnt2)
print(otv)



