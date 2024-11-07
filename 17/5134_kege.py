with open('17_5134.txt') as f:
    sp = [int(x) for x in f]
maxx = 0
for x in sp:
    if x % 100 == 10:
        maxx = max(maxx, x)
k = 0
mins = 10000000
for i in range(len(sp) - 1):
    ost1 = sp[i] % 2023
    ost2 = sp[i + 1] % 2023
    pr = ost1 * ost2
    if pr >= maxx:
        k += 1
        mins = min(mins, sp[i] + sp[i + 1])
print(k)
print(mins)
