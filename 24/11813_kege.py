with open('24_11813.txt') as f:
    f=f.readline()
gl='eyuioa'.upper()
sogl='qwrtpsdfghjklzxcvbnm'.upper()
k=1
maxx=0
for i in range(len(f)-1):
    if not(f[i] in gl and f[i+1] in gl) and \
            not (f[i] in sogl and f[i + 1] in sogl):
        k+=1
        maxx=max(maxx, k)
    else:
        k=1
print(maxx)