with open('st_1_24.txt') as f:
    sp=[[int(x) for x in line.split()] for line in f]
k=0
for x in sp:
    povt=[]
    nepovt=[]
    fl=0
    for y in x:
        if x.count(y)==1:
            nepovt.append(y)
        else:
            povt.append(y)
        if x.count(y)>=3:
            fl=1
    #print(povt, nepovt)
    if fl and len(nepovt) and \
            sum(povt)/len(povt)>sum(nepovt)/len(nepovt):
        k+=1
print(k)



