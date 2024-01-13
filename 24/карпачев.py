with open ('24-6_1.txt') as f:
    f=f.readline()
    f=f.replace('A', '*')
    f=f.replace('E', '*')
    f=f.split('*')
spdl=[]
maxx=0
for x in f:
    spdl.append(len(x))
for i in range(len(f)):
    maxx=max(maxx, sum(spdl[i:i+100]))
print(maxx+100)

