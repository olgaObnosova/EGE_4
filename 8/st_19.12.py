import itertools as f
s=list(f.product('12345678', repeat=11))
k=0
for x in s:
    x=''.join(x)
    if x.count('1')<=4 and x.count('2')<=4 and x.count('3')<=4 and \
       x.count('4')<=4 and x.count('5')<=4 and x.count('6')<=4 and \
       x.count('6')<=4 and x.count('7')<=4 and x.count('8')<=4:
        fl=1
        for i in range(len(x)-1):
            if int(x[i])%2==int(x[i+1])%2:
                fl=0
            if fl:
                k+=1
print(k)