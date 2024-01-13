import itertools as f
s=list(f.permutations('0123456789ABCDEF', r=4))
k=0
for x in s:
    x=''.join(x)
    if x[0]!='0' and x.count('2')*2+x.count('4')*4+\
            x.count('6')*6+x.count('8')*8+\
            x.count('A')*10+x.count('C')*12+\
            x.count('E')*14== \
       x.count('1')+x.count('3')*3+\
            x.count('5')*5+x.count('7')*7+\
            x.count('9')*9+x.count('B')*11+\
            x.count('D')*13+x.count('F')*15:

        x=x.replace('2', '*')
        x = x.replace('0', '*')
        x=x.replace('4', '*')
        x=x.replace('6', '*')
        x=x.replace('8', '*')
        x=x.replace('A', '*')
        x=x.replace('C', '*')
        x=x.replace('E', '*')
        x=x.replace('1', '#')
        x=x.replace('3', '#')
        x=x.replace('5', '#')
        x=x.replace('7', '#')
        x=x.replace('9', '#')
        x=x.replace('B', '#')
        x=x.replace('D', '#')
        x=x.replace('F', '#')
        if x.count('*')==2 and x.count('#')==2:
            k+=1
print(k)