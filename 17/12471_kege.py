with open('17_12471.txt') as f:
   sp = [int(x) for x in f]
maxx = k = s = 0
for x in sp:
    if x%100==13:
       maxx = max(maxx, x)
for i in range(len(sp)-2):
   if ((sp[i]%2==0 and sp[i+1]%2==0 and sp[i+2]==0)\
      or (9 < sp[i]<100 or len(str(sp[i+1]))==2 or\
      9< sp[i+2] < 100)) and sp[i]+sp[i+1]+sp[i+2]<=maxx:
      k+=1
      s+=sp[i]+sp[i+1]+sp[i+2]
print(k)
print(s/k)




