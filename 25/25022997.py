import fnmatch as f
for i in range(220050,10**7):
    if f.fnmatch(str(i),'22?0*5?') and i%111==0:
        print(i, i//111)