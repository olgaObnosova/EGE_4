with open('9_4.txt') as f:
    sp=[[int(y) for y in x.split()] for x in f]
k=0
for x in sp:
    k+=1
    povt=[]
    if x[0]<=x[1]<=x[2]<=x[3]<=x[4]:
        for y in x:
            if x.count(y)>1:
                povt.append(y)
        if len(povt)>0:
            print(povt, k)