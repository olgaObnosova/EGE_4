with open('27A_11796.txt') as f:
    n = f.readline().split()
    k = int(n[1])
    m = int(n[2])
    ch = [int(line) for line in f]
mx1 = mx = mxc = 0
sp=[0]*m # 42
for i in range(len(ch) - k):
    sp[ch[i]%m] = max(sp[ch[i]%m] , ch[i]) #45
    mx = max(mx, sp[(m-ch[i + k]%m)%m] + ch[i + k]) #42-0
print(mx)
