from functools import *
@lru_cache(None)
def f(x, k):
    if k==68:
        ans.add(x)
        return
    f(x+3, k+1)
    f(x -2, k + 1)
ans=set()
f(1, 0)
print(len(ans))
