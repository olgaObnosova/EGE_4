import fnmatch as f
# for i in range(12453, 10**8):
#     if i%1756==0:
#         print(i)
#         break
for i in range(14048, 10 ** 8, 1756):
    if f.fnmatch(str(i), '*12*45*3*'):
        print(i, i//1756)