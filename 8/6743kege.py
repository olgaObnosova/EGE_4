k = 0
for x1 in 'айкос':
    for x2 in 'айкос':
        for x3 in 'айкос':
            for x4 in 'айкос':
                for x5 in 'айкос':
                    x = x1 + x2 + x3 + x4 + x5
                    k += 1
                    if 'сс' not in x and \
                            x.count('о') < 2:
                        print(k)
