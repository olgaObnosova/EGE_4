a='8'*60+'4'*60+'6'*60
while '46' in a or '84' in a or '86' in a:
    if '46' in a:
        a=a.replace('46','64',1)
    if '84' in a:
        a=a.replace('84','48',1)
    if '86' in a:
        a=a.replace('86','68',1)
print(a[25], a[75], a[150])