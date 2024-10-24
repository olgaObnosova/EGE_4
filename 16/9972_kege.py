sp=[0]*4203
for i in range(len(sp)):
    if i<=2:
        sp[i]=2**i
    elif i>2 and i%2==0:
        sp[i]=sp[i//2]
    else:
        sp[i]+=sp[i-4]
for i in range(len(sp)-1, 2, -1):
    if i>2 and i%2!=0:
        sp[i]+=sp[i+1]
print(sp[4202])
# def f(n):
#     if n<=2:
#         return 2**n
#     elif n>2 and n%2==0:
#         return f(n//2)
#     return f(n+1)+f(n-4)
# sp=[]
# for x in range(900, 1000):
#     sp.append(f(x))
#     if f(x)==908430860:
#         print(x)
# print(sp)