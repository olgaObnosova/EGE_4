with open('26_8168.txt') as f:
    k = int(f.readline())
    n = int(f.readline())
    sp = []
    for x in f:
        a, b = map(int, x.split())
        sp.append([a, b])
sp.sort()
count = 0
kam = [0] * k
print(sp[-10:])
vr = 0
for x in sp:
    st, end = x
    #if 0 not in kam:
        #print(kam, min(kam))
        #print(st, end) #186+534=720
    for i in range(k):
        if st >= kam[i] + 1:
            #print(kam)
            kam[i] = st + end
            count+=1
            break
print(count)
