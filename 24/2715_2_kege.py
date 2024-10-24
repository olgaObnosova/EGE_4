with open('24_2715.txt') as f:  # DEV мин
    f=f.readline() # FIN макс DF EF
k=0
f=f.replace('D','*') #DEF
f=f.replace('E','*')
f=f.replace('V','*')
f=f.replace('F','@')
f=f.replace('I','@')
f=f.replace('N','@')
for i in range(len(f)-1):
    if f[i]+f[i+1]=='*@' or f[i]+f[i+1]=='@*' :
        k+=1
print(k)
