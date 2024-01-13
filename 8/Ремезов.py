import itertools as f
s=list(f.permutations ('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', r=3))
k=0

for x in s:
    x=''.join(x)
    if x[0]!='0' and \
       x.count('0')+x.count('2')+x.count('4')+x.count('6')+ \
       x.count('8')+x.count('A')+x.count('C')+ \
       x.count('E')+x.count('G')+x.count('I')+ \
       x.count('K')+x.count('M')+x.count('O')+ \
       x.count('Q')+x.count('S')+x.count('U')+ \
       x.count('W')+x.count('Y')> \
       x.count('1')+x.count('3')+x.count('5')+ \
       x.count('7')+x.count('9')+x.count('B')+ \
       x.count('D')+x.count('F')+x.count('H')+ \
       x.count('J')+x.count('L')+x.count('N')+ \
       x.count('P')+x.count('R')+x.count('T')+ \
       x.count('V')+x.count('X')+x.count('Z'):
        fl=1
        for i in range(len(x)-1):
            if (int(x[i],36)%2==0 and int(x[i+1],36)%2==0)\
                or (int(x[i],36)%2==1 and int(x[i+1],36)%2==1):
                fl=0
        if fl:
            k+=1
print(k)