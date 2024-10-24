# import sys
# sys.setrecursionlimit(100000)
# def f(n):
#     if n<=10:
#         return n*2
#     elif n>10 and n%2==0:
#         return f(n-3)-f(n-9)*2
#     else:
#         return f(n-2)*2-f(n-7)
# print(f(3063))
sp=[0]*3064
for i in range(len(sp)):
    if i<=10:
        sp[i]=i*2
    elif i>10 and i%2==0:
        sp[i]=sp[i-3]-sp[i-9]*2
    else:
        sp[i]=sp[i-2]*2-sp[i-7]
print(sum(map(int, str(sp[3063]))))