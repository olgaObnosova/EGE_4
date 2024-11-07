import fnmatch as f
for i in range(32540262, 10**13, 519):
  if len(str(i))%2==0 and '0' not in str(i) \
          and f.fnmatch(str(i),'32*54?123'):
      pl=len(str(i))//2
      s1=sum([int(x) for x in str(i)[:pl]])
      s2 = sum([int(x) for x in str(i)[pl:]])
      if s1==s2:
          print(i, i//519)

