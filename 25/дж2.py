
import fnmatch as f
for i in range (2468035, 10**9):
    if i%13==0:
        print(i)
        break
for i in range(2468037, 10**9, 13):#24*68?35
   x=str(i)
   if int(x[-3])%2!=0 and int(x[-3])%3==0 and '1' not in x[2:-5]\
       and '3' not in x[2:-5] and '5' not in x[2:-5]\
       and '7' not in x[2:-5] and '9' not in x[2:-5] \
           and x[-2:]=='35' and x[:2]=='24' and x[-5:-3]=='68':
        print(i, i//13)