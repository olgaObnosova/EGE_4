a='3'*50+'6'*50+'9'*50
while '63' in a or '69' in a or '93' in a:
    if '63' in a:
        a=a.replace('63','36', 1)
    if '69' in a:
        a=a.replace('69','96', 1)
    if '93' in a:
        a=a.replace('93', '39', 1)
print(a[41],a[99],a[143])