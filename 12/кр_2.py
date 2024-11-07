def pr(i):
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            return False
    return True
minn=float('inf')
for n in range(1, 1000):
    if pr(n):
        a='1'+'2'* n
        #print(a)
        while '221' in a or '2' in a:
            if '221' in a:
                a=a.replace('221','54321', 1)
            elif'2' in a:
                a=a.replace('2','11', 1)
        if len(a)==5:
            print(n, a)
            minn=min(minn, n)
print(minn)