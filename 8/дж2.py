import itertools as f
s=list(f.product('0234689ACE', repeat=5))
k=0
for x in s:
    x=''.join(x)
    if x[0]!='0' and ((int(x[0], 15)%2==0 and int(x[1], 15)%3==0 and \
                      int(x[2], 15) % 2 == 0 and int(x[3], 15)%3==0 and \
                      int(x[4], 15) % 2 == 0) or (int(x[0], 15)%3==0 and \
                                                  int(x[1], 15)%2==0 and \
                      int(x[2], 15) % 3 == 0 and int(x[3], 15)%2==0 and \
                      int(x[4], 15) % 3 == 0)):
        k+=1
print(k)