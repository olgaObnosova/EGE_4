maxx=0
for n in range(0,256):
    r = bin(n)[2:]
    t = 8 - len(r)
    r = '0' * t + r
    r2 = r[::-1]
    razn=int(r, 2) - int(r2,2)
    maxx=max(maxx, razn)
print(maxx)
