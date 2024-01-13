import itertools as f
k=0
for x in list(f.product('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', repeat=8)):
    k+=1
    x=''.join(x)
    if x=='РЕКУРСИЯ':
        print(k)
        break