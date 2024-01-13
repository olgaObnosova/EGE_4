with open('24_9075.txt') as f:
    f=f.readline()
for x in '02468':
    f=f.replace(x,"*")
for x in '13579':
    f=f.replace(x,"@")
f=f.split('**')
maxx = 0
for x in f:
    x=x.split('@@')
    for j in x:
        if len(j)>maxx:
            maxx=len(j)
            otv=j
print(maxx)
print(otv)

# k=1
# maxx=0
# s=''
# for i in range(len(f)-1):
#     if f[i] in '0123456789' and f[i+1] in '0123456789':
#         if int(f[i])%2!=int(f[i+1])%2:
#             k+=1
#             s+=f[i]
#             if k>maxx:
#                 maxx=k
#                 otv=s
#         else:
#             k=1
#             s=''
#     else: #b08
#         k+=1
#         s += f[i] #b0
#         if k > maxx:
#             maxx = k
#             otv = s
#
# print(maxx)
# print(otv)
print(list(map(int,['1','2'])))