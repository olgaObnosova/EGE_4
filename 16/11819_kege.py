
import sys
sys.setrecursionlimit(10000)
def f(n):
    if n<10:
        return n
    else:
        return g(f(n-1)%10)+f(g(n%10)-1)-f(n-3)
def g(n):
    if n<10:
        return -n
    else:
        return f(g(n-1)%10)+g(f(n-1)-1)+g(n-2)
print(f(1111)+g(1111))
'''
sp=[0]*1112
sg=[0]*1112
for i in range(len(sp)):
    if i<10:
        sp[i]=i
        sg[i]=-i
    else:
        sg[i] = sp[sg[i - 1] % 10] + sg[sp[i - 1] - 1] - sg[i - 2]
        sp[i]=sg[sp[i-1]%10]+sp[sg[i%10]-1]-sp[i-3]
        #sg[i]=sp[sg[i-1]%10]+sg[sp[i-1]-1]-sg[i-2]
print(sp[1111]+sg[1111])
print(sp[:50])
print(sg[:50])
'''