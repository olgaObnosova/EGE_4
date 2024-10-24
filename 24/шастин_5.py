with open('24-sh.txt') as f:
    f = f.readline()
    f = f.replace('1', '*')
    f = f.replace('3', '*')
    f = f.replace('5', '*')
    f = f.replace('7', '*')
    f = f.replace('9', '*')
    f = f.split('***')
maxx = 0
print(len(f))
k=0
for x in f:
    if len(x)>maxx:
        maxx=len(x)
        otv=x
        ind=k

    k+=1
print(maxx+4)
#print(otv)
print(ind)