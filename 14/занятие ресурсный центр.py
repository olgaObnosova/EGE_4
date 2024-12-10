import string as s
dig = s.digits + s.ascii_uppercase
print(dig)
def cn_10(n, b):
    n = n[::-1]
    k = 0
    for i in range(len(n)):
        k += n[i] * b**i
    return k

def conv(n, b):
    s=[]
    while n!=0:
        s.append(n%b)
        n=n//b
    return s[::-1]
print(conv(23, 2))
for x in range(95):
    for y in range(95):
        a=[1,x,y,x,5]
        b=[6,y,x,1,7]
        a_10=cn_10(a, 95)
        b_10=cn_10(b, 95)
        if(a_10+b_10)%4221==0:
            print(hex((a_10+b_10)//4221), (a_10+b_10)//4221, x, y)