with open('27B-4.txt') as f:
    n = int(f.readline())
    spo = [float('inf')]*144
    minn = float('inf')
    for x in f:
        x = int(x)
        ost = x % 144 #1
        if int(x) > spo[(144-ost) % 144]:
            minn = min(x + spo[(144 - ost) % 144], minn)
        spo[ost] = min(spo[ost], x)
print(minn)