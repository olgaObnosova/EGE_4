# k=0
# def f(n):
#     global k
#     if n<=2:
#         k+=1
#         return 2
#     else:
#         k+=1
#         return f(n-1)-2*f(n-2)
# f(57)
# print(k)
sp=[0]*58
for i in range(1, 58):
    if i<=2:
        sp[i]=1
    else:
        sp[i]=sp[i-1]+sp[i-2]+1
print(sp)
