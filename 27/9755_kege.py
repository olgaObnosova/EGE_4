with open('27_B_9755.txt') as f:
    k = int(f.readline())
    n = int(f.readline())
    sp = [int(x) for x in f]
min1 = mins1 = mins = float('inf')
for i in range(0, len(sp)-2*k):
    min1 = min(min1, sp[i])
    mins1 = min(mins1, min1+sp[i+k])
    mins = min(mins, mins1+sp[i + 2 * k])
print(mins)