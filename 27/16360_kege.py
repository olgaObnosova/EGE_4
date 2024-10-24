with open('pr') as f:
    n=int(f.readline())
    sp=[int(x)//3+bool(int(x)%3) for x in f]
