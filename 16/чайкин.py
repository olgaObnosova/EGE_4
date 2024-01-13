'''
def f(n):
    if n == 0:
        return 0
    elif int(n ** 0.5) == n**0.5:
        return f(n - 1) - n
    else:
        return f(n - 1) + n


print(f(77555533))
'''
sp=[0]*77555534
for i in range(len(sp)):
    if i==0:
        sp[i]=0
    elif int(i**0.5)==i**0.5:
        sp[i]=sp[i-1]-i
    else:
        sp[i]=sp[i-1]+i

print(sp[77555533])
