def pr(n):
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True
k=0
for i in range(10**7,10**8):
    if pr(i):
        print(abs(10**7-i), i)
        k+=1
        if k==5:
            break