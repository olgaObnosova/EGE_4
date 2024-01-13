with open('24.txt') as f:
    f=f.readline()
print('ATGTTTGTCAAACATAA' in f)
print(f.find('ATGTTTGTCAAACATAA'))
print(f[11143:11160])
print(len('ATGTTTGTCAAACATAA'))
f=f.split('ACATAA')
#print(len(f))
for x in f[:-1]:
    x=x.split('ATGTTT')
    if 'TAA' not in x[-1] \
            and 'TGA' not in x[-1] \
            and 'TAG' not in x[-1]:
                l=x[-1]
                print(l)