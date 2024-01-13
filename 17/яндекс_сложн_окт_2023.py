with open('17yan.txt') as f:
    sp = []
    maxx = 0
    for x in f:
        sp.append(int(x))


def pal(n):
    if str(n)==str(n)[::-1]:
        return True
    return False
def sumc(n):
    s=0
    while n!=0:
        s+=n%10
        n=n//10
    return s

k = 0
for i in range(len(sp) - 2):
    if (len(str(sp[i])) == 4 and len(str(sp[i + 1])) == 4\
        and len(str(sp[i + 2])) == 4) and \
            (sumc(sp[i])!=sumc(sp[i+1]) and \
             sumc(sp[i])!=sumc(sp[i+2])\
        and sumc(sp[i+1])!=sumc(sp[i+2])) and \
            pal(sp[i] + sp[i + 1] + sp[i + 2]):
        k += 1
        maxx = max(maxx, sumc(sp[i]),sumc(sp[i + 1]),sumc(sp[i + 2]))
print(k, maxx)
