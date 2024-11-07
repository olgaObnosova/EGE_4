# def f(n):
#     if n<=2:
#         return 1
#     elif n>2 and n%2!=0:
#         return f(n-1)-n
#     else:
#         return f(n-2)+g(n-1)+2
# def g(n):
#     if n<=0:
#         return 2
#     elif n>2 and n%2!=0:
#         return f(n-1)-2*g(n-2)
#     else:
#         return 2*f(n-2)-2*g(n-1)
# print(f(96))
f=[0]*97
g=[0]*97
f[0]=1
f[1]=1
f[2]=1
g[0]=2
g[1]=1-2*2
for i in range(2, 97):
    if i>2 and i%2!=0:
        f[i]=f[i-1]-i
    if i > 2 and i % 2 == 0:
        f[i]=f[i-2]+g[i-1]+2
    if i>0 and i%2!=0:
        g[i]=f[i-1]-2*g[i-2]
    if i > 0 and i % 2 == 0:
        g[i]=2*f[i-2]-2*g[i-1]
print(f[96])