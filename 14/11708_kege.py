s=0
for i in range(16, 16**2):
    if i%4==3:
        #print(hex(i))
        s+=i
print(s)
def f(n):
    s=0
    for x in str(n):
        s+=int(x)
    return s
print(f(123))
