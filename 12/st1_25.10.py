def pr(n):
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True
minn=float('inf')
for i in range(100):
    for j in range(100):
        a='0'+i*'1'+j*'2'
        suma=a.count('1')+a.count('2')*2
        l=len(a)
        while '01' in a or '02' in a:
            a=a.replace('02','1110',1)
            a = a.replace('01', '220', 1)
        sumb = a.count('1')+a.count('2')*2
        if l>40 and pr(sumb):
            minn=min(minn, suma)
print(minn)

