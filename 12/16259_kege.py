a='3'+'424'*20+'2'*5+'3' #25*7+15+10
maxx=0

while '3' in a:
    if '342' in a:
        a=a.replace('342', '4123', 1)
    if '34' in a:
        a = a.replace('34', '413', 1)
    if '32' in a:
        a = a.replace('32', '13', 1)
    if '33' in a:
        a = a.replace('33', '424', 1)
k=a.count('1')+a.count('2')*2+a.count('3')*3+a.count('4')*4
print(a)
print(k)