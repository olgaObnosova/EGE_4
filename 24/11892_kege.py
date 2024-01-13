with open('24_11892.txt') as f:
    f = f.readline().strip()
    f = f.split('Y')
minn = 9999999999 #xxxxx, xxxxx, xxxx
#print(f[:5])
for x in f:
    x=x.strip()
    if x.count('X')>=500:
        minn=min(minn, len(x.strip()))
print(minn)
