import fnmatch as f

for i in range(12579, 10**9, 21):
    if f.fnmatch(str(i),'1*5*9'):
        ch=str(i)
        fl=1
        for j in range(len(ch)-1):
            if ch[j]>=ch[j+1]:
                fl=0
        if fl:
            print(i, i//21)
#144 - 1 143
#mins=min(mins,x+sp[(144-x%144)%144])
#ost[x%144]=min(ost[x%144], x)