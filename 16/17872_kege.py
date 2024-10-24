'''def f(n):
    if n==1:
        return 1
    return (n-1)*f(n-1)
print((f(2024)+2*f(2023))/f(2022))
'''
sp=[0]*2025
for n in range(2025):
    if n==1:
        sp[n]=1
    elif n>1:
        sp[n]=(n-1)*sp[n-1]
print((sp[2024]+2*sp[2023])//sp[2022])
