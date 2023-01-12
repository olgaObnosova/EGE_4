with open('27_A.txt') as f:
    n, k, m = map(int, f.readline().split())
    road = []
    let = []
    for _ in range(n):
        km, lets = map(int, f.readline().split())
        road.extend([km, km + k])
        let.append((lets + 8) // 9)
    let += let
    # print(let)
    road.sort()
    # print(road)
