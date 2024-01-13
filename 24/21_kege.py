with open('24_21.txt') as f:
    f = f.readline()
maxx = 0
f = f.replace('XX','**')
f = f.replace('YY','**')
f = f.replace('ZZ','**')
f = f.split('**') #YY,XYXXXXXY
for x in f:
    maxx = max(maxx, len(x))
print(maxx)

