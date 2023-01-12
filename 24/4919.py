with open('4919.txt') as f:
    cntt=0
    f = f.readline().split('B')
    #print(len(f))
    for x in f:
        #print(x)
        if len(x)>18 and x[0]=='A' and x.count('F')==2 and x.count('A')==1:
            cntt+=1
            #cntt+=(len(x)-18)
        elif len(x)>18:
            n = x.find('A')
            
            if n!=-1 and len(x[n:])>18 and x[n:].count('A')==1 \
               and x.count('F')==2:
                #print(x[n:])
                cntt+=1
                #cntt+=(len(x[n:])-18)
                
        
print(cntt)
   
    
                    
        
