with open('24-9.txt') as f:
    f=f.readline()
f=f.replace('A','@')
f=f.replace('E','@')
f=f.replace('B','*')
f=f.replace('C','*')
f=f.replace('D','*')
f=f.replace('F','*')
f=f.replace('G','*')
f=f.replace('H','*')
f=f.split('**@')
maxl=0
for x in f:
    maxl=max(maxl, len(x))
print(maxl)
