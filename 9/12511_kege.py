with open('12511') as f:
    k=0
    for x in f:
        spp = []
        spn = []
        sp=[int(y) for y in x.split()]
        for z in sp:
            if sp.count(z)==2:
                spp.append(z)
            else:
                spn.append(z)
        if len(spp)==6 and sum(spp)/len(spp)>spn[0]:
            k+=1
print(k)
