for i in range(6, 100):
    a = 7 ** 500 - 5 * i + 3
    if a % 6 == 0:
        print(i)
        break
