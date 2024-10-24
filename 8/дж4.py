import itertools as t

otv=set()
for i in range(5**4,5**5-1):
    for j in range(i+1,5**5):
        c = j-i
        otv.add(c)
#print(otv[:10])
print(len(otv))
