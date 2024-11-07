def f(a,k):
    if k==15:
        ans.add(a)
        return
    f(a+10, k+1)
    f(a-5, k+1)
ans=set()
f(1,0)
print(ans)
