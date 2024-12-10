alf='0123456789'
buk='qwertyuiopasdfghjklzxcvbnm'
buk=sorted(buk)
buk=''.join(buk)
alf=alf+buk
for x in alf:
    a = int(f'9ah{x}p', 36) + int('aaab5', 23)-\
        int(f'lol{x}', 36)
    if a%76==0:
        print(a, alf.find(x))