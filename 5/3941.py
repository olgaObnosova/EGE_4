k=0
for i in range(1,1000):
    n=bin(i)[2:]
    print(n)
    if n[-1]=='0':
        n = n[:-1]+n[:2]
        print(n[:-1])
        break
    n=n[::-1]
    if int(n,2)==127:
        k+=1
print(k)