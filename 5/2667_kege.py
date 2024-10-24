minn=float('inf')

for k in range(1, 10000):
    b = bin(k)[2:]
    #print(b)
    b += str(b.count('1') % 2)
    #print(b)
    b += b[-1]
    #print(b)
    r = int(b, 2)
    if r > 60:
        minn = min(minn, k)
print(minn)