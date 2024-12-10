for x in range(1, 256):
    n=bin(x)[2:]
    dl = 8 - len(n)
    n='0' * dl + n
    nom = n.rfind('1')
    n = n[:nom].replace('1', '2') + n[nom:]
    n = n[:nom].replace('0', '1') + n[nom:]
    n = n[:nom].replace('2', '0') + n[nom:]
    r=int(n, 2)
    if r==171:
        print(x)