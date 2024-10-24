import sys
sys.setrecursionlimit(1000)
def f(st, ed, s):
    if st>ed or st==6:
        return 0
    elif st==ed and 'aa' not in s and 'bb' not in s\
            and 'cc' not in s:
        return 1
    else:
        return f(st+1, ed, s+'a')+f(st+3, ed, s+'b')\
               +f(st**2, ed, s+'c')
print(f(2, 5, '') * f(5, 25, ''))